import datetime

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_response_payload_handler',
        'Scrum.utils.jwt_response_payload_handler',

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=1),

    # pass the prefix + token in the authorization header ("Authorization": "JWT " + token)
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,
}