import boto3

'''
ensure that you have installed aws cli by running the command 
pip install awscli 

Also install aws-shell and configure the workspace using
htps://aws.amazon.com/cli/
'''

'''
ensure that you have ~/.aws/credentials file filled with <aws_access_key_id>, <aws_secret_access_key>
'''

ec2 = boto3.resource('ec2')

response = ec2.create_instances(ImageId='ami-0cd3dfa4e37921605', 
                        MinCount=1, 
                        MaxCount=1, 
                        InstanceType='t2.micro', 
                        SecurityGroups=['security_gg'], 
                        KeyName='gg')


print ("Instance_id", response[0].instance_id)
print ("public IP_address", response[0].public_ip_address)
print ("secrity_groups", response[0].security_groups)
print ("placement_region", response[0].placement)



# client = boto3.client('ec2')
# '''
# Stop instance
# '''
# client.stop_instances(InstanceIds=['<instance-id>'])

# '''
# Terminate instance
# '''
# client.terminate_instances(InstanceIds=['<instance-id>'])