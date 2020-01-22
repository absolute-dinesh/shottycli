import boto3
import click

session = boto3.Session(profile_name = 'dinesh-amaze')
ec2 = session.resource('ec2')


@click.group()
def instances():
    """Commands for instances"""


@instances.command('list')
@click.option('--project',default=None,
    help="only instances for project")
def list_instances(project):
    '''Putting help message with click decorator,
    this function is listing info on list_instances'''
    instances = []

    if project:
        filters = [{'Name':'tag:project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags = {t['Key']:t['Value'] for t in i.tags or []}
        print(' ,'.join(
        (i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name,
        tags.get('project','<project>'))
        ))
    return


@instances.command('stop')
@click.option('--project', default=None)
def stop_instances(project):
    '''Putting help message with click decorator,
    this function is listing info on list_instances'''
    instances = []

    if project:
        filters = [{'Name':'tag:project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()

    return



if __name__ == '__main__':
    instances()
