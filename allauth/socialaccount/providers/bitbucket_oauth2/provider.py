from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class BitbucketOAuth2Account(ProviderAccount):
    pass


class BitbucketOAuth2Provider(OAuth2Provider):
    id = 'bitbucket_oauth2'
    name = 'Bitbucket'
    package = 'allauth.socialaccount.providers.bitbucket_oauth2'
    account_class = BitbucketOAuth2Account

    def extract_uid(self, data):
        return data['username']

    def extract_common_fields(self, data):
        return dict(name=data.get('display_name'))

providers.registry.register(BitbucketOAuth2Provider)
