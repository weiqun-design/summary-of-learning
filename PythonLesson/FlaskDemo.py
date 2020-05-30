from flask import Flask
from flask import logging
from logging import FileHandler
from For_OKP_test.CreateOrder.CreateOrderFromAtomeAppOkpVersion import atome_app_okp_profile
from For_OKP_test.CreateOrder.NkpRejectCreateCreditApplication import nkp_reject_profile
from For_OKP_test.CreateOrder.SendCoupon import send_coupon_profile
from For_OKP_test.CreateOrder.tokopedia_create_order import tokopedia_create_order_profile
from For_OKP_test.CreateOrder.BimaCreateOrder import create_bima_order_profile
from For_OKP_test.CreateOrder.LoanIntentionFromNKP import loan_intention_from_nkp_profile
from For_OKP_test.CreateOrder.TcashCreateOrder import tcash_order_profile
from For_OKP_test.CreateOrder.BukalapakCreateOrder import bukalapak_create_order_profile
from For_OKP_test.CreateOrder.H5CreateOrder import atome_h5_create_order_profile
from For_OKP_test.CreateOrder.AtomeCreateSecondOrder import create_second_order_from_atome_app_profile
from For_OKP_test.CreateOrder.CreateOkpNkpOngoingOrder import okp_nkp_ongoing_order_profile
from For_OKP_test.CreateOrder.PosLoan import pos_loan_profile
from For_OKP_test.Tool.XmindToCSV import xmind_to_csv_profile


app = Flask(__name__)
app.register_blueprint(atome_app_okp_profile, url_prefix='/atome/okp/')
app.register_blueprint(nkp_reject_profile, url_prefix='/nkp/reject/')
app.register_blueprint(tokopedia_create_order_profile)
app.register_blueprint(create_bima_order_profile)
app.register_blueprint(loan_intention_from_nkp_profile)
app.register_blueprint(tcash_order_profile)
app.register_blueprint(bukalapak_create_order_profile)
app.register_blueprint(atome_h5_create_order_profile)
app.register_blueprint(create_second_order_from_atome_app_profile)
app.register_blueprint(send_coupon_profile)
app.register_blueprint(okp_nkp_ongoing_order_profile)
app.register_blueprint(pos_loan_profile)
app.register_blueprint(xmind_to_csv_profile)


#解决中文乱码的问题，将json数据内的中文正常显示
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    handler = FileHandler('app.log')
    handler.setLevel(20)
    app.logger.addHandler(handler)
    app.run()

