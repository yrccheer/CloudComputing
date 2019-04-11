import boto3

ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-088e1a6468669e557')

print("instance_public_ip", instance.public_ip_address)
# print("instance_region", instance.placement)
print("instance_ID", instance.instance_id)
