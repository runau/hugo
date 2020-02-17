```uml
@startuml
!define AWSPUML https://raw.githubusercontent.com/milo-minderbinder/AWS-PlantUML/release/18-2-22/dist
!includeurl AWSPUML/common.puml
!includeurl AWSPUML/Compute/AWSLambda/AWSLambda.puml
!includeurl AWSPUML/General/AWScloud/AWScloud.puml
!includeurl AWSPUML/General/user/user.puml
!includeurl AWSPUML/Storage/AmazonS3/AmazonS3.puml
!includeurl AWSPUML/General/traditionalserver/traditionalserver.puml
!includeurl AWSPUML/NetworkingContentDelivery/AmazonRoute53/AmazonRoute53.puml

!includeurl AWSPUML/Messaging/AmazonSES/AmazonSES.puml
!includeurl AWSPUML/Messaging/AmazonSNS/AmazonSNS.puml
!includeurl AWSPUML/Messaging/AmazonSQS/AmazonSQS.puml

skinparam componentArrowColor Black
skinparam componentBackgroundColor White
skinparam nodeBackgroundColor White
skinparam agentBackgroundColor White
skinparam artifactBackgroundColor White


USER(user)
TRADITIONALSERVER(server,server)
AWSCLOUD(aws) {
 AMAZONROUTE53(route)
 AMAZONS3(s3) 
 AMAZONSES(ses)
 AMAZONSNS(sns)
 AMAZONSQS(sqs)
 AWSLAMBDA(lambda) 
}

server -d-> route
route -d-> ses
ses -d-> sns
ses -d-> s3
sns -d-> sqs
sqs -d-> lambda
lambda -d-> user

@enduml
```
