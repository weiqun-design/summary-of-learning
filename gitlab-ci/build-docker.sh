#!/bin/bash
set -e
set -x

DIR="$( cd "$(dirname "$0")" ; pwd -P )"
cd $DIR

APPLICATION_VERSION=`cat ./APPLICATION_VERSION`  # staging-202002201506-f3b7ee6
IMAGE_BASE_NAME=docker.advai.net/billing-center
MODULES=('application-service' 'application-scheduled')
for m in "${MODULES[@]}"; do
    IMAGE_NAME=${IMAGE_BASE_NAME}/${m}
    IMAGE_NAME_WITH_TAG=$IMAGE_NAME:${APPLICATION_VERSION}
    DEST_DIR=${DIR}/${m}/build/libs
    cp ${DIR}/Dockerfile $DEST_DIR/Dockerfile
    sed -i "s/TO_BE_REPLACED/$m/g" $DEST_DIR/Dockerfile
    cp $DIR/logback-spring.xml $DEST_DIR/
    cd $DEST_DIR
    echo "exec java \$JAVA_OPTS -jar /app/$m.jar" > startup.sh
    LATEST_TAG=$CI_COMMIT_REF_NAME-latest
    docker build --build-arg APPLICATION_VERSION=${APPLICATION_VERSION} -t $IMAGE_NAME:$LATEST_TAG $DEST_DIR
    if [[ $CI_COMMIT_REF_NAME == master* ]]; then
        docker tag $IMAGE_NAME:$LATEST_TAG $IMAGE_NAME:${APPLICATION_VERSION}
        docker push $IMAGE_NAME:${APPLICATION_VERSION}
    fi
done