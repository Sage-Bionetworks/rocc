from datetime import date

from mongoengine import connect, disconnect

from openapi_server.dbmodels.organization import Organization
from openapi_server.dbmodels.person import Person
from openapi_server.dbmodels.tag import Tag
from openapi_server.dbmodels.grant import Grant
from openapi_server.dbmodels.challenge import Challenge
from openapi_server.dbmodels.challenge_results import ChallengeResults
from openapi_server.dbmodels.user import User


def connect_db():
    connect('mongoenginetest', host='mongomock://localhost')


def disconnect_db():
    disconnect(alias='mongoenginetest')


def create_test_tag(tag_id):
    return Tag(tagId=tag_id).save()


def create_test_organization(organization_id):
    return Organization(
        organizationId=organization_id,
        name="Awesome Organization",
        shortName="AO",
        url="https://awesome-organization.org"
    ).save()


def create_test_person(organizations):
    return Person(
        firstName="Awesome",
        lastName="Person",
        email="awesome-person@example.org",
        organizations=organizations
    ).save()


def create_test_user(username, organizations):
    return User(
        username=username,
        firstName="Awesome",
        lastName="Person",
        email="awesome-person@example.org",
        organizations=organizations
    ).save()


def create_test_grant():
    return Grant(
        name="awesome-grant",
        description="description",
        url="https://report.nih.gov/"
    ).save()


def create_test_challenge_results():
    return ChallengeResults(
        nSubmissions=0,
        nFinalSubmissions=0,
        nRegisteredParticipants=0
    )


def create_test_challenge(organizers, tags):
    return Challenge(
        name="awesome-challenge",
        startDate=date(2020, 12, 1),
        endDate=date(2020, 12, 31),
        url="https://www.synapse.org/",
        status="upcoming",
        organizers=organizers,
        tags=tags,
        challengeResults=create_test_challenge_results().to_dict()
    ).save()
