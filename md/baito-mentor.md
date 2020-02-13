```uml
@startuml
!define AWSPUML https://raw.githubusercontent.com/milo-minderbinder/AWS-PlantUML/release/18-2-22/dist
!includeurl AWSPUML/common.puml
!includeurl AWSPUML/ApplicationServices/AmazonAPIGateway/AmazonAPIGateway.puml
!includeurl AWSPUML/Compute/AWSLambda/AWSLambda.puml
!includeurl AWSPUML/Database/AmazonDynamoDB/AmazonDynamoDB.puml
!includeurl AWSPUML/General/AWScloud/AWScloud.puml
!includeurl AWSPUML/General/client/client.puml
!includeurl AWSPUML/General/mobileclient/mobileclient.puml
!includeurl AWSPUML/General/user/user.puml
!includeurl AWSPUML/Storage/AmazonS3/AmazonS3.puml
!includeurl AWSPUML/Storage/AmazonS3/bucket/bucket.puml
!includeurl AWSPUML/General/traditionalserver/traditionalserver.puml
!includeurl AWSPUML/NetworkingContentDelivery/AmazonCloudFront/AmazonCloudFront.puml
!includeurl AWSPUML/NetworkingContentDelivery/AmazonCloudFront/downloaddistribution/downloaddistribution.puml
!includeurl AWSPUML/NetworkingContentDelivery/AmazonRoute53/AmazonRoute53.puml
!includeurl AWSPUML/NetworkingContentDelivery/AmazonRoute53/hostedzone/hostedzone.puml
skinparam componentArrowColor Black
skinparam componentBackgroundColor White
skinparam nodeBackgroundColor White
skinparam agentBackgroundColor White
skinparam artifactBackgroundColor White

USER(user)
MOBILECLIENT(line,line)
TRADITIONALSERVER(messagingApi,line messaging api)
TRADITIONALSERVER(lineLogin,line login)
AWSCLOUD(aws) {
 AMAZONROUTE53(route)
 AMAZONS3(s3) 
 AMAZONAPIGATEWAY(api)
 AWSLAMBDA(lambda) 
 AMAZONDYNAMODB(dynamo) 
 AMAZONCLOUDFRONT(cloudFront)
}
user -d-> line
user <-d- line

lineLogin -d-> line
lineLogin <-d- line

line -d-> messagingApi
line <-d- messagingApi

api -d-> lambda
api <-d- lambda

lambda -d-> s3

s3 -d-> cloudFront
s3 <-d- cloudFront

cloudFront -d-> route
cloudFront <-d- route

messagingApi <-d- api
messagingApi -d-> api

route -d-> lineLogin
route <-d- lineLogin

lambda -d-> dynamo
lambda <-d- dynamo

@enduml
```
