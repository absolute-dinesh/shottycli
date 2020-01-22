import boto3
import click

session = boto3.Session(profile_name = 'dinesh-amaze')
ec2 = session.resource('ec2')


#decorator
@click.command()
def list_instances():
    '''Putting help message with click decorator,
    this function is listing info on list_instances'''
    for i in ec2.instances.all():
        print(' ,'.join(
        (i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name)
        ))
    return

if __name__ == '__main__':
    list_instances()
