import boto3
import datetime
import argparse
#from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--profile", help="input profile", required=True)
parser.add_argument("--region", help="input region", required=True)
#parser.add_argument("--Key", help="tag key ", required=True)
#parser.add_argument("--Value", help="tag Value ", required=True)
args = parser.parse_args()
profile= args.profile
region= args.region
#tag= args.tag
#key= args.key


session = boto3.session.Session(profile_name=profile)
client_ec2= session.client('ec2',region_name=region)
client = session.client('cloudtrail',region_name=region)
Attributes=[
    {
        'AttributeKey': 'EventName',
        'AttributeValue': 'RunInstances'
    },
]
trailresponse = client.lookup_events(LookupAttributes=Attributes,MaxResults=1)
#totat_instances=(len(ec2response['Reservations']))
#print(len(trailresponse['Events'][0]['Resources']))

# for i in range(0,len(trailresponse['Events'][0]['Resources'])):
#     if(trailresponse['Events'][0]['Resources'][i]['ResourceType']=='AWS::EC2::Instance'):
#         print(trailresponse['Events'][0]['Resources'][i]['ResourceName'])


response = client_ec2.associate_iam_instance_profile(
    IamInstanceProfile={
        'Arn': 'arn:aws:iam::089816662102:instance-profile/SSMRole'
    },
    InstanceId='i-0bee6ba336df12f9d'
)
print(response)
