from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['phone'] = user.phone
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['avatar'] = user.avatar
        token['role'] = user.role
        token['biology'] = user.biology
        token['address'] = user.address
        return token