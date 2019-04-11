from botocore.exceptions import ClientError
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
	response = ec2.create_security_group(GroupName = 'security_gg',
										 Description = 'security group for cloud computing',
										 VpcId = vpc_id)
	security_group_id = response['GroupId']
	print ('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

	data = ec2.authorize_security_group_ingress(
		GroupId = security_group_id,
		IpPermissions = [
			{'IpProtocol' : 'tcp',
			 'FromPort' : 22,
			 'ToPort' : 22,
			 'IpRanges' : [{'CidrIp' : '0.0.0.0/0'}]}

		])
except ClientError as e:
	print(e)