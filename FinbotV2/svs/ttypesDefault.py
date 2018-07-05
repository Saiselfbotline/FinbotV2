from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
import sys

from FinbotServer.transport import TTransport

class ApplicationType(object):
    IOS = 16
    IOS_RC = 17
    IOS_BETA = 18
    IOS_ALPHA = 19
    ANDROID = 32
    ANDROID_RC = 33
    ANDROID_BETA = 34
    ANDROID_ALPHA = 35
    WAP = 48
    WAP_RC = 49
    WAP_BETA = 50
    WAP_ALPHA = 51
    BOT = 64
    BOT_RC = 65
    BOT_BETA = 66
    BOT_ALPHA = 67
    WEB = 80
    WEB_RC = 81
    WEB_BETA = 82
    WEB_ALPHA = 83
    DESKTOPWIN = 96
    DESKTOPWIN_RC = 97
    DESKTOPWIN_BETA = 98
    DESKTOPWIN_ALPHA = 99
    DESKTOPMAC = 112
    DESKTOPMAC_RC = 113
    DESKTOPMAC_BETA = 114
    DESKTOPMAC_ALPHA = 115
    CHANNELGW = 128
    CHANNELGW_RC = 129
    CHANNELGW_BETA = 130
    CHANNELGW_ALPHA = 131
    CHANNELCP = 144
    CHANNELCP_RC = 145
    CHANNELCP_BETA = 146
    CHANNELCP_ALPHA = 147
    WINPHONE = 160
    WINPHONE_RC = 161
    WINPHONE_BETA = 162
    WINPHONE_ALPHA = 163
    BLACKBERRY = 176
    BLACKBERRY_RC = 177
    BLACKBERRY_BETA = 178
    BLACKBERRY_ALPHA = 179
    WINMETRO = 192
    WINMETRO_RC = 193
    WINMETRO_BETA = 194
    WINMETRO_ALPHA = 195
    S40 = 208
    S40_RC = 209
    S40_BETA = 210
    S40_ALPHA = 211
    CHRONO = 224
    CHRONO_RC = 225
    CHRONO_BETA = 226
    CHRONO_ALPHA = 227
    TIZEN = 256
    TIZEN_RC = 257
    TIZEN_BETA = 258
    TIZEN_ALPHA = 259
    VIRTUAL = 272

    _VALUES_TO_NAMES = {
        16: "IOS",
        17: "IOS_RC",
        18: "IOS_BETA",
        19: "IOS_ALPHA",
        32: "ANDROID",
        33: "ANDROID_RC",
        34: "ANDROID_BETA",
        35: "ANDROID_ALPHA",
        48: "WAP",
        49: "WAP_RC",
        50: "WAP_BETA",
        51: "WAP_ALPHA",
        64: "BOT",
        65: "BOT_RC",
        66: "BOT_BETA",
        67: "BOT_ALPHA",
        80: "WEB",
        81: "WEB_RC",
        82: "WEB_BETA",
        83: "WEB_ALPHA",
        96: "DESKTOPWIN",
        97: "DESKTOPWIN_RC",
        98: "DESKTOPWIN_BETA",
        99: "DESKTOPWIN_ALPHA",
        112: "DESKTOPMAC",
        113: "DESKTOPMAC_RC",
        114: "DESKTOPMAC_BETA",
        115: "DESKTOPMAC_ALPHA",
        128: "CHANNELGW",
        129: "CHANNELGW_RC",
        130: "CHANNELGW_BETA",
        131: "CHANNELGW_ALPHA",
        144: "CHANNELCP",
        145: "CHANNELCP_RC",
        146: "CHANNELCP_BETA",
        147: "CHANNELCP_ALPHA",
        160: "WINPHONE",
        161: "WINPHONE_RC",
        162: "WINPHONE_BETA",
        163: "WINPHONE_ALPHA",
        176: "BLACKBERRY",
        177: "BLACKBERRY_RC",
        178: "BLACKBERRY_BETA",
        179: "BLACKBERRY_ALPHA",
        192: "WINMETRO",
        193: "WINMETRO_RC",
        194: "WINMETRO_BETA",
        195: "WINMETRO_ALPHA",
        208: "S40",
        209: "S40_RC",
        210: "S40_BETA",
        211: "S40_ALPHA",
        224: "CHRONO",
        225: "CHRONO_RC",
        226: "CHRONO_BETA",
        227: "CHRONO_ALPHA",
        256: "TIZEN",
        257: "TIZEN_RC",
        258: "TIZEN_BETA",
        259: "TIZEN_ALPHA",
        272: "VIRTUAL",
    }

    _NAMES_TO_VALUES = {
        "IOS": 16,
        "IOS_RC": 17,
        "IOS_BETA": 18,
        "IOS_ALPHA": 19,
        "ANDROID": 32,
        "ANDROID_RC": 33,
        "ANDROID_BETA": 34,
        "ANDROID_ALPHA": 35,
        "WAP": 48,
        "WAP_RC": 49,
        "WAP_BETA": 50,
        "WAP_ALPHA": 51,
        "BOT": 64,
        "BOT_RC": 65,
        "BOT_BETA": 66,
        "BOT_ALPHA": 67,
        "WEB": 80,
        "WEB_RC": 81,
        "WEB_BETA": 82,
        "WEB_ALPHA": 83,
        "DESKTOPWIN": 96,
        "DESKTOPWIN_RC": 97,
        "DESKTOPWIN_BETA": 98,
        "DESKTOPWIN_ALPHA": 99,
        "DESKTOPMAC": 112,
        "DESKTOPMAC_RC": 113,
        "DESKTOPMAC_BETA": 114,
        "DESKTOPMAC_ALPHA": 115,
        "CHANNELGW": 128,
        "CHANNELGW_RC": 129,
        "CHANNELGW_BETA": 130,
        "CHANNELGW_ALPHA": 131,
        "CHANNELCP": 144,
        "CHANNELCP_RC": 145,
        "CHANNELCP_BETA": 146,
        "CHANNELCP_ALPHA": 147,
        "WINPHONE": 160,
        "WINPHONE_RC": 161,
        "WINPHONE_BETA": 162,
        "WINPHONE_ALPHA": 163,
        "BLACKBERRY": 176,
        "BLACKBERRY_RC": 177,
        "BLACKBERRY_BETA": 178,
        "BLACKBERRY_ALPHA": 179,
        "WINMETRO": 192,
        "WINMETRO_RC": 193,
        "WINMETRO_BETA": 194,
        "WINMETRO_ALPHA": 195,
        "S40": 208,
        "S40_RC": 209,
        "S40_BETA": 210,
        "S40_ALPHA": 211,
        "CHRONO": 224,
        "CHRONO_RC": 225,
        "CHRONO_BETA": 226,
        "CHRONO_ALPHA": 227,
        "TIZEN": 256,
        "TIZEN_RC": 257,
        "TIZEN_BETA": 258,
        "TIZEN_ALPHA": 259,
        "VIRTUAL": 272,
    }


class BuddyBannerLinkType(object):
    BUDDY_BANNER_LINK_HIDDEN = 0
    BUDDY_BANNER_LINK_MID = 1
    BUDDY_BANNER_LINK_URL = 2

    _VALUES_TO_NAMES = {
        0: "BUDDY_BANNER_LINK_HIDDEN",
        1: "BUDDY_BANNER_LINK_MID",
        2: "BUDDY_BANNER_LINK_URL",
    }

    _NAMES_TO_VALUES = {
        "BUDDY_BANNER_LINK_HIDDEN": 0,
        "BUDDY_BANNER_LINK_MID": 1,
        "BUDDY_BANNER_LINK_URL": 2,
    }


class BuddyOnAirType(object):
    NORMAL = 0
    LIVE = 1
    VOIP = 2

    _VALUES_TO_NAMES = {
        0: "NORMAL",
        1: "LIVE",
        2: "VOIP",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 0,
        "LIVE": 1,
        "VOIP": 2,
    }


class BuddyResultState(object):
    ACCEPTED = 1
    SUCCEEDED = 2
    FAILED = 3
    CANCELLED = 4
    NOTIFY_FAILED = 5
    STORING = 11
    UPLOADING = 21
    NOTIFYING = 31

    _VALUES_TO_NAMES = {
        1: "ACCEPTED",
        2: "SUCCEEDED",
        3: "FAILED",
        4: "CANCELLED",
        5: "NOTIFY_FAILED",
        11: "STORING",
        21: "UPLOADING",
        31: "NOTIFYING",
    }

    _NAMES_TO_VALUES = {
        "ACCEPTED": 1,
        "SUCCEEDED": 2,
        "FAILED": 3,
        "CANCELLED": 4,
        "NOTIFY_FAILED": 5,
        "STORING": 11,
        "UPLOADING": 21,
        "NOTIFYING": 31,
    }


class BuddySearchRequestSource(object):
    NA = 0
    FRIEND_VIEW = 1
    OFFICIAL_ACCOUNT_VIEW = 2

    _VALUES_TO_NAMES = {
        0: "NA",
        1: "FRIEND_VIEW",
        2: "OFFICIAL_ACCOUNT_VIEW",
    }

    _NAMES_TO_VALUES = {
        "NA": 0,
        "FRIEND_VIEW": 1,
        "OFFICIAL_ACCOUNT_VIEW": 2,
    }


class CarrierCode(object):
    NOT_SPECIFIED = 0
    JP_DOCOMO = 1
    JP_AU = 2
    JP_SOFTBANK = 3
    KR_SKT = 17
    KR_KT = 18
    KR_LGT = 19

    _VALUES_TO_NAMES = {
        0: "NOT_SPECIFIED",
        1: "JP_DOCOMO",
        2: "JP_AU",
        3: "JP_SOFTBANK",
        17: "KR_SKT",
        18: "KR_KT",
        19: "KR_LGT",
    }

    _NAMES_TO_VALUES = {
        "NOT_SPECIFIED": 0,
        "JP_DOCOMO": 1,
        "JP_AU": 2,
        "JP_SOFTBANK": 3,
        "KR_SKT": 17,
        "KR_KT": 18,
        "KR_LGT": 19,
    }


class ChannelConfiguration(object):
    MESSAGE = 0
    MESSAGE_NOTIFICATION = 1
    NOTIFICATION_CENTER = 2

    _VALUES_TO_NAMES = {
        0: "MESSAGE",
        1: "MESSAGE_NOTIFICATION",
        2: "NOTIFICATION_CENTER",
    }

    _NAMES_TO_VALUES = {
        "MESSAGE": 0,
        "MESSAGE_NOTIFICATION": 1,
        "NOTIFICATION_CENTER": 2,
    }


class ChannelErrorCode(object):
    ILLEGAL_ARGUMENT = 0
    INTERNAL_ERROR = 1
    CONNECTION_ERROR = 2
    AUTHENTICATIONI_FAILED = 3
    NEED_PERMISSION_APPROVAL = 4
    COIN_NOT_USABLE = 5

    _VALUES_TO_NAMES = {
        0: "ILLEGAL_ARGUMENT",
        1: "INTERNAL_ERROR",
        2: "CONNECTION_ERROR",
        3: "AUTHENTICATIONI_FAILED",
        4: "NEED_PERMISSION_APPROVAL",
        5: "COIN_NOT_USABLE",
    }

    _NAMES_TO_VALUES = {
        "ILLEGAL_ARGUMENT": 0,
        "INTERNAL_ERROR": 1,
        "CONNECTION_ERROR": 2,
        "AUTHENTICATIONI_FAILED": 3,
        "NEED_PERMISSION_APPROVAL": 4,
        "COIN_NOT_USABLE": 5,
    }


class ChannelSyncType(object):
    SYNC = 0
    REMOVE = 1

    _VALUES_TO_NAMES = {
        0: "SYNC",
        1: "REMOVE",
    }

    _NAMES_TO_VALUES = {
        "SYNC": 0,
        "REMOVE": 1,
    }


class ContactAttribute(object):
    CONTACT_ATTRIBUTE_CAPABLE_VOICE_CALL = 1
    CONTACT_ATTRIBUTE_CAPABLE_VIDEO_CALL = 2
    CONTACT_ATTRIBUTE_CAPABLE_MY_HOME = 16
    CONTACT_ATTRIBUTE_CAPABLE_BUDDY = 32

    _VALUES_TO_NAMES = {
        1: "CONTACT_ATTRIBUTE_CAPABLE_VOICE_CALL",
        2: "CONTACT_ATTRIBUTE_CAPABLE_VIDEO_CALL",
        16: "CONTACT_ATTRIBUTE_CAPABLE_MY_HOME",
        32: "CONTACT_ATTRIBUTE_CAPABLE_BUDDY",
    }

    _NAMES_TO_VALUES = {
        "CONTACT_ATTRIBUTE_CAPABLE_VOICE_CALL": 1,
        "CONTACT_ATTRIBUTE_CAPABLE_VIDEO_CALL": 2,
        "CONTACT_ATTRIBUTE_CAPABLE_MY_HOME": 16,
        "CONTACT_ATTRIBUTE_CAPABLE_BUDDY": 32,
    }


class ContactCategory(object):
    NORMAL = 0
    RECOMMEND = 1

    _VALUES_TO_NAMES = {
        0: "NORMAL",
        1: "RECOMMEND",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 0,
        "RECOMMEND": 1,
    }


class ContactRelation(object):
    ONEWAY = 0
    BOTH = 1
    NOT_REGISTERED = 2

    _VALUES_TO_NAMES = {
        0: "ONEWAY",
        1: "BOTH",
        2: "NOT_REGISTERED",
    }

    _NAMES_TO_VALUES = {
        "ONEWAY": 0,
        "BOTH": 1,
        "NOT_REGISTERED": 2,
    }


class ContactSetting(object):
    CONTACT_SETTING_NOTIFICATION_DISABLE = 1
    CONTACT_SETTING_DISPLAY_NAME_OVERRIDE = 2
    CONTACT_SETTING_CONTACT_HIDE = 4
    CONTACT_SETTING_FAVORITE = 8
    CONTACT_SETTING_DELETE = 16

    _VALUES_TO_NAMES = {
        1: "CONTACT_SETTING_NOTIFICATION_DISABLE",
        2: "CONTACT_SETTING_DISPLAY_NAME_OVERRIDE",
        4: "CONTACT_SETTING_CONTACT_HIDE",
        8: "CONTACT_SETTING_FAVORITE",
        16: "CONTACT_SETTING_DELETE",
    }

    _NAMES_TO_VALUES = {
        "CONTACT_SETTING_NOTIFICATION_DISABLE": 1,
        "CONTACT_SETTING_DISPLAY_NAME_OVERRIDE": 2,
        "CONTACT_SETTING_CONTACT_HIDE": 4,
        "CONTACT_SETTING_FAVORITE": 8,
        "CONTACT_SETTING_DELETE": 16,
    }


class ContactStatus(object):
    UNSPECIFIED = 0
    FRIEND = 1
    FRIEND_BLOCKED = 2
    RECOMMEND = 3
    RECOMMEND_BLOCKED = 4
    DELETED = 5
    DELETED_BLOCKED = 6

    _VALUES_TO_NAMES = {
        0: "UNSPECIFIED",
        1: "FRIEND",
        2: "FRIEND_BLOCKED",
        3: "RECOMMEND",
        4: "RECOMMEND_BLOCKED",
        5: "DELETED",
        6: "DELETED_BLOCKED",
    }

    _NAMES_TO_VALUES = {
        "UNSPECIFIED": 0,
        "FRIEND": 1,
        "FRIEND_BLOCKED": 2,
        "RECOMMEND": 3,
        "RECOMMEND_BLOCKED": 4,
        "DELETED": 5,
        "DELETED_BLOCKED": 6,
    }


class ContactType(object):
    MID = 0
    PHONE = 1
    EMAIL = 2
    USERID = 3
    PROXIMITY = 4
    GROUP = 5
    USER = 6
    QRCODE = 7
    PROMOTION_BOT = 8
    REPAIR = 128
    FACEBOOK = 2305
    SINA = 2306
    RENREN = 2307
    FEIXIN = 2308

    _VALUES_TO_NAMES = {
        0: "MID",
        1: "PHONE",
        2: "EMAIL",
        3: "USERID",
        4: "PROXIMITY",
        5: "GROUP",
        6: "USER",
        7: "QRCODE",
        8: "PROMOTION_BOT",
        128: "REPAIR",
        2305: "FACEBOOK",
        2306: "SINA",
        2307: "RENREN",
        2308: "FEIXIN",
    }

    _NAMES_TO_VALUES = {
        "MID": 0,
        "PHONE": 1,
        "EMAIL": 2,
        "USERID": 3,
        "PROXIMITY": 4,
        "GROUP": 5,
        "USER": 6,
        "QRCODE": 7,
        "PROMOTION_BOT": 8,
        "REPAIR": 128,
        "FACEBOOK": 2305,
        "SINA": 2306,
        "RENREN": 2307,
        "FEIXIN": 2308,
    }


class ContentType(object):
    NONE = 0
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    HTML = 4
    PDF = 5
    CALL = 6
    STICKER = 7
    PRESENCE = 8
    GIFT = 9
    GROUPBOARD = 10
    APPLINK = 11
    LINK = 12
    CONTACT = 13
    FILE = 14
    LOCATION = 15
    POSTNOTIFICATION = 16
    RICH = 17
    CHATEVENT = 18

    _VALUES_TO_NAMES = {
        0: "NONE",
        1: "IMAGE",
        2: "VIDEO",
        3: "AUDIO",
        4: "HTML",
        5: "PDF",
        6: "CALL",
        7: "STICKER",
        8: "PRESENCE",
        9: "GIFT",
        10: "GROUPBOARD",
        11: "APPLINK",
        12: "LINK",
        13: "CONTACT",
        14: "FILE",
        15: "LOCATION",
        16: "POSTNOTIFICATION",
        17: "RICH",
        18: "CHATEVENT",
    }

    _NAMES_TO_VALUES = {
        "NONE": 0,
        "IMAGE": 1,
        "VIDEO": 2,
        "AUDIO": 3,
        "HTML": 4,
        "PDF": 5,
        "CALL": 6,
        "STICKER": 7,
        "PRESENCE": 8,
        "GIFT": 9,
        "GROUPBOARD": 10,
        "APPLINK": 11,
        "LINK": 12,
        "CONTACT": 13,
        "FILE": 14,
        "LOCATION": 15,
        "POSTNOTIFICATION": 16,
        "RICH": 17,
        "CHATEVENT": 18,
    }


class CustomMode(object):
    PROMOTION_FRIENDS_INVITE = 1
    CAPABILITY_SERVER_SIDE_SMS = 2
    LINE_CLIENT_ANALYTICS_CONFIGURATION = 3

    _VALUES_TO_NAMES = {
        1: "PROMOTION_FRIENDS_INVITE",
        2: "CAPABILITY_SERVER_SIDE_SMS",
        3: "LINE_CLIENT_ANALYTICS_CONFIGURATION",
    }

    _NAMES_TO_VALUES = {
        "PROMOTION_FRIENDS_INVITE": 1,
        "CAPABILITY_SERVER_SIDE_SMS": 2,
        "LINE_CLIENT_ANALYTICS_CONFIGURATION": 3,
    }


class EmailConfirmationStatus(object):
    NOT_SPECIFIED = 0
    NOT_YET = 1
    DONE = 3

    _VALUES_TO_NAMES = {
        0: "NOT_SPECIFIED",
        1: "NOT_YET",
        3: "DONE",
    }

    _NAMES_TO_VALUES = {
        "NOT_SPECIFIED": 0,
        "NOT_YET": 1,
        "DONE": 3,
    }


class EmailConfirmationType(object):
    SERVER_SIDE_EMAIL = 0
    CLIENT_SIDE_EMAIL = 1

    _VALUES_TO_NAMES = {
        0: "SERVER_SIDE_EMAIL",
        1: "CLIENT_SIDE_EMAIL",
    }

    _NAMES_TO_VALUES = {
        "SERVER_SIDE_EMAIL": 0,
        "CLIENT_SIDE_EMAIL": 1,
    }


class ErrorCode(object):
    ILLEGAL_ARGUMENT = 0
    AUTHENTICATION_FAILED = 1
    DB_FAILED = 2
    INVALID_STATE = 3
    EXCESSIVE_ACCESS = 4
    NOT_FOUND = 5
    INVALID_LENGTH = 6
    NOT_AVAILABLE_USER = 7
    NOT_AUTHORIZED_DEVICE = 8
    INVALID_MID = 9
    NOT_A_MEMBER = 10
    INCOMPATIBLE_APP_VERSION = 11
    NOT_READY = 12
    NOT_AVAILABLE_SESSION = 13
    NOT_AUTHORIZED_SESSION = 14
    SYSTEM_ERROR = 15
    NO_AVAILABLE_VERIFICATION_METHOD = 16
    NOT_AUTHENTICATED = 17
    INVALID_IDENTITY_CREDENTIAL = 18
    NOT_AVAILABLE_IDENTITY_IDENTIFIER = 19
    INTERNAL_ERROR = 20
    NO_SUCH_IDENTITY_IDENFIER = 21
    DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY = 22
    ILLEGAL_IDENTITY_CREDENTIAL = 23
    UNKNOWN_CHANNEL = 24
    NO_SUCH_MESSAGE_BOX = 25
    NOT_AVAILABLE_MESSAGE_BOX = 26
    CHANNEL_DOES_NOT_MATCH = 27
    NOT_YOUR_MESSAGE = 28
    MESSAGE_DEFINED_ERROR = 29
    USER_CANNOT_ACCEPT_PRESENTS = 30
    USER_NOT_STICKER_OWNER = 32
    MAINTENANCE_ERROR = 33
    ACCOUNT_NOT_MATCHED = 34
    ABUSE_BLOCK = 35
    NOT_FRIEND = 36
    NOT_ALLOWED_CALL = 37
    BLOCK_FRIEND = 38
    INCOMPATIBLE_VOIP_VERSION = 39
    INVALID_SNS_ACCESS_TOKEN = 40
    EXTERNAL_SERVICE_NOT_AVAILABLE = 41
    NOT_ALLOWED_ADD_CONTACT = 42
    NOT_CERTIFICATED = 43
    NOT_ALLOWED_SECONDARY_DEVICE = 44
    INVALID_PIN_CODE = 45
    NOT_FOUND_IDENTITY_CREDENTIAL = 46
    EXCEED_FILE_MAX_SIZE = 47
    EXCEED_DAILY_QUOTA = 48
    NOT_SUPPORT_SEND_FILE = 49
    MUST_UPGRADE = 50
    NOT_AVAILABLE_PIN_CODE_SESSION = 51

    _VALUES_TO_NAMES = {
        0: "ILLEGAL_ARGUMENT",
        1: "AUTHENTICATION_FAILED",
        2: "DB_FAILED",
        3: "INVALID_STATE",
        4: "EXCESSIVE_ACCESS",
        5: "NOT_FOUND",
        6: "INVALID_LENGTH",
        7: "NOT_AVAILABLE_USER",
        8: "NOT_AUTHORIZED_DEVICE",
        9: "INVALID_MID",
        10: "NOT_A_MEMBER",
        11: "INCOMPATIBLE_APP_VERSION",
        12: "NOT_READY",
        13: "NOT_AVAILABLE_SESSION",
        14: "NOT_AUTHORIZED_SESSION",
        15: "SYSTEM_ERROR",
        16: "NO_AVAILABLE_VERIFICATION_METHOD",
        17: "NOT_AUTHENTICATED",
        18: "INVALID_IDENTITY_CREDENTIAL",
        19: "NOT_AVAILABLE_IDENTITY_IDENTIFIER",
        20: "INTERNAL_ERROR",
        21: "NO_SUCH_IDENTITY_IDENFIER",
        22: "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY",
        23: "ILLEGAL_IDENTITY_CREDENTIAL",
        24: "UNKNOWN_CHANNEL",
        25: "NO_SUCH_MESSAGE_BOX",
        26: "NOT_AVAILABLE_MESSAGE_BOX",
        27: "CHANNEL_DOES_NOT_MATCH",
        28: "NOT_YOUR_MESSAGE",
        29: "MESSAGE_DEFINED_ERROR",
        30: "USER_CANNOT_ACCEPT_PRESENTS",
        32: "USER_NOT_STICKER_OWNER",
        33: "MAINTENANCE_ERROR",
        34: "ACCOUNT_NOT_MATCHED",
        35: "ABUSE_BLOCK",
        36: "NOT_FRIEND",
        37: "NOT_ALLOWED_CALL",
        38: "BLOCK_FRIEND",
        39: "INCOMPATIBLE_VOIP_VERSION",
        40: "INVALID_SNS_ACCESS_TOKEN",
        41: "EXTERNAL_SERVICE_NOT_AVAILABLE",
        42: "NOT_ALLOWED_ADD_CONTACT",
        43: "NOT_CERTIFICATED",
        44: "NOT_ALLOWED_SECONDARY_DEVICE",
        45: "INVALID_PIN_CODE",
        46: "NOT_FOUND_IDENTITY_CREDENTIAL",
        47: "EXCEED_FILE_MAX_SIZE",
        48: "EXCEED_DAILY_QUOTA",
        49: "NOT_SUPPORT_SEND_FILE",
        50: "MUST_UPGRADE",
        51: "NOT_AVAILABLE_PIN_CODE_SESSION",
    }

    _NAMES_TO_VALUES = {
        "ILLEGAL_ARGUMENT": 0,
        "AUTHENTICATION_FAILED": 1,
        "DB_FAILED": 2,
        "INVALID_STATE": 3,
        "EXCESSIVE_ACCESS": 4,
        "NOT_FOUND": 5,
        "INVALID_LENGTH": 6,
        "NOT_AVAILABLE_USER": 7,
        "NOT_AUTHORIZED_DEVICE": 8,
        "INVALID_MID": 9,
        "NOT_A_MEMBER": 10,
        "INCOMPATIBLE_APP_VERSION": 11,
        "NOT_READY": 12,
        "NOT_AVAILABLE_SESSION": 13,
        "NOT_AUTHORIZED_SESSION": 14,
        "SYSTEM_ERROR": 15,
        "NO_AVAILABLE_VERIFICATION_METHOD": 16,
        "NOT_AUTHENTICATED": 17,
        "INVALID_IDENTITY_CREDENTIAL": 18,
        "NOT_AVAILABLE_IDENTITY_IDENTIFIER": 19,
        "INTERNAL_ERROR": 20,
        "NO_SUCH_IDENTITY_IDENFIER": 21,
        "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY": 22,
        "ILLEGAL_IDENTITY_CREDENTIAL": 23,
        "UNKNOWN_CHANNEL": 24,
        "NO_SUCH_MESSAGE_BOX": 25,
        "NOT_AVAILABLE_MESSAGE_BOX": 26,
        "CHANNEL_DOES_NOT_MATCH": 27,
        "NOT_YOUR_MESSAGE": 28,
        "MESSAGE_DEFINED_ERROR": 29,
        "USER_CANNOT_ACCEPT_PRESENTS": 30,
        "USER_NOT_STICKER_OWNER": 32,
        "MAINTENANCE_ERROR": 33,
        "ACCOUNT_NOT_MATCHED": 34,
        "ABUSE_BLOCK": 35,
        "NOT_FRIEND": 36,
        "NOT_ALLOWED_CALL": 37,
        "BLOCK_FRIEND": 38,
        "INCOMPATIBLE_VOIP_VERSION": 39,
        "INVALID_SNS_ACCESS_TOKEN": 40,
        "EXTERNAL_SERVICE_NOT_AVAILABLE": 41,
        "NOT_ALLOWED_ADD_CONTACT": 42,
        "NOT_CERTIFICATED": 43,
        "NOT_ALLOWED_SECONDARY_DEVICE": 44,
        "INVALID_PIN_CODE": 45,
        "NOT_FOUND_IDENTITY_CREDENTIAL": 46,
        "EXCEED_FILE_MAX_SIZE": 47,
        "EXCEED_DAILY_QUOTA": 48,
        "NOT_SUPPORT_SEND_FILE": 49,
        "MUST_UPGRADE": 50,
        "NOT_AVAILABLE_PIN_CODE_SESSION": 51,
    }


class FeatureType(object):
    OBJECT_STORAGE = 1

    _VALUES_TO_NAMES = {
        1: "OBJECT_STORAGE",
    }

    _NAMES_TO_VALUES = {
        "OBJECT_STORAGE": 1,
    }


class GroupAttribute(object):
    NAME = 1
    PICTURE_STATUS = 2
    ALL = 255

    _VALUES_TO_NAMES = {
        1: "NAME",
        2: "PICTURE_STATUS",
        255: "ALL",
    }

    _NAMES_TO_VALUES = {
        "NAME": 1,
        "PICTURE_STATUS": 2,
        "ALL": 255,
    }


class IdentityProvider(object):
    UNKNOWN = 0
    LINE = 1
    NAVER_KR = 2

    _VALUES_TO_NAMES = {
        0: "UNKNOWN",
        1: "LINE",
        2: "NAVER_KR",
    }

    _NAMES_TO_VALUES = {
        "UNKNOWN": 0,
        "LINE": 1,
        "NAVER_KR": 2,
    }


class LoginResultType(object):
    SUCCESS = 1
    REQUIRE_QRCODE = 2
    REQUIRE_DEVICE_CONFIRM = 3

    _VALUES_TO_NAMES = {
        1: "SUCCESS",
        2: "REQUIRE_QRCODE",
        3: "REQUIRE_DEVICE_CONFIRM",
    }

    _NAMES_TO_VALUES = {
        "SUCCESS": 1,
        "REQUIRE_QRCODE": 2,
        "REQUIRE_DEVICE_CONFIRM": 3,
    }


class MessageOperationType(object):
    SEND_MESSAGE = 1
    RECEIVE_MESSAGE = 2
    READ_MESSAGE = 3
    NOTIFIED_READ_MESSAGE = 4
    NOTIFIED_JOIN_CHAT = 5
    FAILED_SEND_MESSAGE = 6
    SEND_CONTENT = 7
    SEND_CONTENT_RECEIPT = 8
    SEND_CHAT_REMOVED = 9
    REMOVE_ALL_MESSAGES = 10

    _VALUES_TO_NAMES = {
        1: "SEND_MESSAGE",
        2: "RECEIVE_MESSAGE",
        3: "READ_MESSAGE",
        4: "NOTIFIED_READ_MESSAGE",
        5: "NOTIFIED_JOIN_CHAT",
        6: "FAILED_SEND_MESSAGE",
        7: "SEND_CONTENT",
        8: "SEND_CONTENT_RECEIPT",
        9: "SEND_CHAT_REMOVED",
        10: "REMOVE_ALL_MESSAGES",
    }

    _NAMES_TO_VALUES = {
        "SEND_MESSAGE": 1,
        "RECEIVE_MESSAGE": 2,
        "READ_MESSAGE": 3,
        "NOTIFIED_READ_MESSAGE": 4,
        "NOTIFIED_JOIN_CHAT": 5,
        "FAILED_SEND_MESSAGE": 6,
        "SEND_CONTENT": 7,
        "SEND_CONTENT_RECEIPT": 8,
        "SEND_CHAT_REMOVED": 9,
        "REMOVE_ALL_MESSAGES": 10,
    }


class MIDType(object):
    USER = 0
    ROOM = 1
    GROUP = 2

    _VALUES_TO_NAMES = {
        0: "USER",
        1: "ROOM",
        2: "GROUP",
    }

    _NAMES_TO_VALUES = {
        "USER": 0,
        "ROOM": 1,
        "GROUP": 2,
    }


class ModificationType(object):
    ADD = 0
    REMOVE = 1
    MODIFY = 2

    _VALUES_TO_NAMES = {
        0: "ADD",
        1: "REMOVE",
        2: "MODIFY",
    }

    _NAMES_TO_VALUES = {
        "ADD": 0,
        "REMOVE": 1,
        "MODIFY": 2,
    }


class NotificationItemFetchMode(object):
    ALL = 0
    APPEND = 1

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "APPEND",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "APPEND": 1,
    }


class NotificationQueueType(object):
    GLOBAL = 1
    MESSAGE = 2
    PRIMARY = 3

    _VALUES_TO_NAMES = {
        1: "GLOBAL",
        2: "MESSAGE",
        3: "PRIMARY",
    }

    _NAMES_TO_VALUES = {
        "GLOBAL": 1,
        "MESSAGE": 2,
        "PRIMARY": 3,
    }


class NotificationStatus(object):
    NOTIFICATION_ITEM_EXIST = 1
    TIMELINE_ITEM_EXIST = 2
    NOTE_GROUP_NEW_ITEM_EXIST = 4
    TIMELINE_BUDDYGROUP_CHANGED = 8
    NOTE_ONE_TO_ONE_NEW_ITEM_EXIST = 16
    ALBUM_ITEM_EXIST = 32
    TIMELINE_ITEM_DELETED = 64

    _VALUES_TO_NAMES = {
        1: "NOTIFICATION_ITEM_EXIST",
        2: "TIMELINE_ITEM_EXIST",
        4: "NOTE_GROUP_NEW_ITEM_EXIST",
        8: "TIMELINE_BUDDYGROUP_CHANGED",
        16: "NOTE_ONE_TO_ONE_NEW_ITEM_EXIST",
        32: "ALBUM_ITEM_EXIST",
        64: "TIMELINE_ITEM_DELETED",
    }

    _NAMES_TO_VALUES = {
        "NOTIFICATION_ITEM_EXIST": 1,
        "TIMELINE_ITEM_EXIST": 2,
        "NOTE_GROUP_NEW_ITEM_EXIST": 4,
        "TIMELINE_BUDDYGROUP_CHANGED": 8,
        "NOTE_ONE_TO_ONE_NEW_ITEM_EXIST": 16,
        "ALBUM_ITEM_EXIST": 32,
        "TIMELINE_ITEM_DELETED": 64,
    }


class NotificationType(object):
    APPLE_APNS = 1
    GOOGLE_C2DM = 2
    NHN_NNI = 3
    SKT_AOM = 4
    MS_MPNS = 5
    RIM_BIS = 6
    GOOGLE_GCM = 7
    NOKIA_NNAPI = 8
    TIZEN = 9
    LINE_BOT = 17
    LINE_WAP = 18

    _VALUES_TO_NAMES = {
        1: "APPLE_APNS",
        2: "GOOGLE_C2DM",
        3: "NHN_NNI",
        4: "SKT_AOM",
        5: "MS_MPNS",
        6: "RIM_BIS",
        7: "GOOGLE_GCM",
        8: "NOKIA_NNAPI",
        9: "TIZEN",
        17: "LINE_BOT",
        18: "LINE_WAP",
    }

    _NAMES_TO_VALUES = {
        "APPLE_APNS": 1,
        "GOOGLE_C2DM": 2,
        "NHN_NNI": 3,
        "SKT_AOM": 4,
        "MS_MPNS": 5,
        "RIM_BIS": 6,
        "GOOGLE_GCM": 7,
        "NOKIA_NNAPI": 8,
        "TIZEN": 9,
        "LINE_BOT": 17,
        "LINE_WAP": 18,
    }


class OpStatus(object):
    NORMAL = 0
    ALERT_DISABLED = 1

    _VALUES_TO_NAMES = {
        0: "NORMAL",
        1: "ALERT_DISABLED",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 0,
        "ALERT_DISABLED": 1,
    }


class OpType(object):
    END_OF_OPERATION = 0
    UPDATE_PROFILE = 1
    NOTIFIED_UPDATE_PROFILE = 2
    REGISTER_USERID = 3
    ADD_CONTACT = 4
    NOTIFIED_ADD_CONTACT = 5
    BLOCK_CONTACT = 6
    UNBLOCK_CONTACT = 7
    NOTIFIED_RECOMMEND_CONTACT = 8
    CREATE_GROUP = 9
    UPDATE_GROUP = 10
    NOTIFIED_UPDATE_GROUP = 11
    INVITE_INTO_GROUP = 12
    NOTIFIED_INVITE_INTO_GROUP = 13
    LEAVE_GROUP = 14
    NOTIFIED_LEAVE_GROUP = 15
    ACCEPT_GROUP_INVITATION = 16
    NOTIFIED_ACCEPT_GROUP_INVITATION = 17
    KICKOUT_FROM_GROUP = 18
    NOTIFIED_KICKOUT_FROM_GROUP = 19
    CREATE_ROOM = 20
    INVITE_INTO_ROOM = 21
    NOTIFIED_INVITE_INTO_ROOM = 22
    LEAVE_ROOM = 23
    NOTIFIED_LEAVE_ROOM = 24
    SEND_MESSAGE = 25
    RECEIVE_MESSAGE = 26
    SEND_MESSAGE_RECEIPT = 27
    RECEIVE_MESSAGE_RECEIPT = 28
    SEND_CONTENT_RECEIPT = 29
    RECEIVE_ANNOUNCEMENT = 30
    CANCEL_INVITATION_GROUP = 31
    NOTIFIED_CANCEL_INVITATION_GROUP = 32
    NOTIFIED_UNREGISTER_USER = 33
    REJECT_GROUP_INVITATION = 34
    NOTIFIED_REJECT_GROUP_INVITATION = 35
    UPDATE_SETTINGS = 36
    NOTIFIED_REGISTER_USER = 37
    INVITE_VIA_EMAIL = 38
    NOTIFIED_REQUEST_RECOVERY = 39
    SEND_CHAT_CHECKED = 40
    SEND_CHAT_REMOVED = 41
    NOTIFIED_FORCE_SYNC = 42
    SEND_CONTENT = 43
    SEND_MESSAGE_MYHOME = 44
    NOTIFIED_UPDATE_CONTENT_PREVIEW = 45
    REMOVE_ALL_MESSAGES = 46
    NOTIFIED_UPDATE_PURCHASES = 47
    DUMMY = 48
    UPDATE_CONTACT = 49
    NOTIFIED_RECEIVED_CALL = 50
    CANCEL_CALL = 51
    NOTIFIED_REDIRECT = 52
    NOTIFIED_CHANNEL_SYNC = 53
    FAILED_SEND_MESSAGE = 54
    NOTIFIED_READ_MESSAGE = 55
    FAILED_EMAIL_CONFIRMATION = 56
    NOTIFIED_CHAT_CONTENT = 58
    NOTIFIED_PUSH_NOTICENTER_ITEM = 59

    _VALUES_TO_NAMES = {
        0: "END_OF_OPERATION",
        1: "UPDATE_PROFILE",
        2: "NOTIFIED_UPDATE_PROFILE",
        3: "REGISTER_USERID",
        4: "ADD_CONTACT",
        5: "NOTIFIED_ADD_CONTACT",
        6: "BLOCK_CONTACT",
        7: "UNBLOCK_CONTACT",
        8: "NOTIFIED_RECOMMEND_CONTACT",
        9: "CREATE_GROUP",
        10: "UPDATE_GROUP",
        11: "NOTIFIED_UPDATE_GROUP",
        12: "INVITE_INTO_GROUP",
        13: "NOTIFIED_INVITE_INTO_GROUP",
        14: "LEAVE_GROUP",
        15: "NOTIFIED_LEAVE_GROUP",
        16: "ACCEPT_GROUP_INVITATION",
        17: "NOTIFIED_ACCEPT_GROUP_INVITATION",
        18: "KICKOUT_FROM_GROUP",
        19: "NOTIFIED_KICKOUT_FROM_GROUP",
        20: "CREATE_ROOM",
        21: "INVITE_INTO_ROOM",
        22: "NOTIFIED_INVITE_INTO_ROOM",
        23: "LEAVE_ROOM",
        24: "NOTIFIED_LEAVE_ROOM",
        25: "SEND_MESSAGE",
        26: "RECEIVE_MESSAGE",
        27: "SEND_MESSAGE_RECEIPT",
        28: "RECEIVE_MESSAGE_RECEIPT",
        29: "SEND_CONTENT_RECEIPT",
        30: "RECEIVE_ANNOUNCEMENT",
        31: "CANCEL_INVITATION_GROUP",
        32: "NOTIFIED_CANCEL_INVITATION_GROUP",
        33: "NOTIFIED_UNREGISTER_USER",
        34: "REJECT_GROUP_INVITATION",
        35: "NOTIFIED_REJECT_GROUP_INVITATION",
        36: "UPDATE_SETTINGS",
        37: "NOTIFIED_REGISTER_USER",
        38: "INVITE_VIA_EMAIL",
        39: "NOTIFIED_REQUEST_RECOVERY",
        40: "SEND_CHAT_CHECKED",
        41: "SEND_CHAT_REMOVED",
        42: "NOTIFIED_FORCE_SYNC",
        43: "SEND_CONTENT",
        44: "SEND_MESSAGE_MYHOME",
        45: "NOTIFIED_UPDATE_CONTENT_PREVIEW",
        46: "REMOVE_ALL_MESSAGES",
        47: "NOTIFIED_UPDATE_PURCHASES",
        48: "DUMMY",
        49: "UPDATE_CONTACT",
        50: "NOTIFIED_RECEIVED_CALL",
        51: "CANCEL_CALL",
        52: "NOTIFIED_REDIRECT",
        53: "NOTIFIED_CHANNEL_SYNC",
        54: "FAILED_SEND_MESSAGE",
        55: "NOTIFIED_READ_MESSAGE",
        56: "FAILED_EMAIL_CONFIRMATION",
        58: "NOTIFIED_CHAT_CONTENT",
        59: "NOTIFIED_PUSH_NOTICENTER_ITEM",
    }

    _NAMES_TO_VALUES = {
        "END_OF_OPERATION": 0,
        "UPDATE_PROFILE": 1,
        "NOTIFIED_UPDATE_PROFILE": 2,
        "REGISTER_USERID": 3,
        "ADD_CONTACT": 4,
        "NOTIFIED_ADD_CONTACT": 5,
        "BLOCK_CONTACT": 6,
        "UNBLOCK_CONTACT": 7,
        "NOTIFIED_RECOMMEND_CONTACT": 8,
        "CREATE_GROUP": 9,
        "UPDATE_GROUP": 10,
        "NOTIFIED_UPDATE_GROUP": 11,
        "INVITE_INTO_GROUP": 12,
        "NOTIFIED_INVITE_INTO_GROUP": 13,
        "LEAVE_GROUP": 14,
        "NOTIFIED_LEAVE_GROUP": 15,
        "ACCEPT_GROUP_INVITATION": 16,
        "NOTIFIED_ACCEPT_GROUP_INVITATION": 17,
        "KICKOUT_FROM_GROUP": 18,
        "NOTIFIED_KICKOUT_FROM_GROUP": 19,
        "CREATE_ROOM": 20,
        "INVITE_INTO_ROOM": 21,
        "NOTIFIED_INVITE_INTO_ROOM": 22,
        "LEAVE_ROOM": 23,
        "NOTIFIED_LEAVE_ROOM": 24,
        "SEND_MESSAGE": 25,
        "RECEIVE_MESSAGE": 26,
        "SEND_MESSAGE_RECEIPT": 27,
        "RECEIVE_MESSAGE_RECEIPT": 28,
        "SEND_CONTENT_RECEIPT": 29,
        "RECEIVE_ANNOUNCEMENT": 30,
        "CANCEL_INVITATION_GROUP": 31,
        "NOTIFIED_CANCEL_INVITATION_GROUP": 32,
        "NOTIFIED_UNREGISTER_USER": 33,
        "REJECT_GROUP_INVITATION": 34,
        "NOTIFIED_REJECT_GROUP_INVITATION": 35,
        "UPDATE_SETTINGS": 36,
        "NOTIFIED_REGISTER_USER": 37,
        "INVITE_VIA_EMAIL": 38,
        "NOTIFIED_REQUEST_RECOVERY": 39,
        "SEND_CHAT_CHECKED": 40,
        "SEND_CHAT_REMOVED": 41,
        "NOTIFIED_FORCE_SYNC": 42,
        "SEND_CONTENT": 43,
        "SEND_MESSAGE_MYHOME": 44,
        "NOTIFIED_UPDATE_CONTENT_PREVIEW": 45,
        "REMOVE_ALL_MESSAGES": 46,
        "NOTIFIED_UPDATE_PURCHASES": 47,
        "DUMMY": 48,
        "UPDATE_CONTACT": 49,
        "NOTIFIED_RECEIVED_CALL": 50,
        "CANCEL_CALL": 51,
        "NOTIFIED_REDIRECT": 52,
        "NOTIFIED_CHANNEL_SYNC": 53,
        "FAILED_SEND_MESSAGE": 54,
        "NOTIFIED_READ_MESSAGE": 55,
        "FAILED_EMAIL_CONFIRMATION": 56,
        "NOTIFIED_CHAT_CONTENT": 58,
        "NOTIFIED_PUSH_NOTICENTER_ITEM": 59,
    }


class PayloadType(object):
    PAYLOAD_BUY = 101
    PAYLOAD_CS = 111
    PAYLOAD_BONUS = 121
    PAYLOAD_EVENT = 131

    _VALUES_TO_NAMES = {
        101: "PAYLOAD_BUY",
        111: "PAYLOAD_CS",
        121: "PAYLOAD_BONUS",
        131: "PAYLOAD_EVENT",
    }

    _NAMES_TO_VALUES = {
        "PAYLOAD_BUY": 101,
        "PAYLOAD_CS": 111,
        "PAYLOAD_BONUS": 121,
        "PAYLOAD_EVENT": 131,
    }


class PaymentPgType(object):
    PAYMENT_PG_NONE = 0
    PAYMENT_PG_AU = 1
    PAYMENT_PG_AL = 2

    _VALUES_TO_NAMES = {
        0: "PAYMENT_PG_NONE",
        1: "PAYMENT_PG_AU",
        2: "PAYMENT_PG_AL",
    }

    _NAMES_TO_VALUES = {
        "PAYMENT_PG_NONE": 0,
        "PAYMENT_PG_AU": 1,
        "PAYMENT_PG_AL": 2,
    }


class PaymentType(object):
    PAYMENT_APPLE = 1
    PAYMENT_GOOGLE = 2

    _VALUES_TO_NAMES = {
        1: "PAYMENT_APPLE",
        2: "PAYMENT_GOOGLE",
    }

    _NAMES_TO_VALUES = {
        "PAYMENT_APPLE": 1,
        "PAYMENT_GOOGLE": 2,
    }


class ProductBannerLinkType(object):
    BANNER_LINK_NONE = 0
    BANNER_LINK_ITEM = 1
    BANNER_LINK_URL = 2
    BANNER_LINK_CATEGORY = 3

    _VALUES_TO_NAMES = {
        0: "BANNER_LINK_NONE",
        1: "BANNER_LINK_ITEM",
        2: "BANNER_LINK_URL",
        3: "BANNER_LINK_CATEGORY",
    }

    _NAMES_TO_VALUES = {
        "BANNER_LINK_NONE": 0,
        "BANNER_LINK_ITEM": 1,
        "BANNER_LINK_URL": 2,
        "BANNER_LINK_CATEGORY": 3,
    }


class ProductEventType(object):
    NO_EVENT = 0
    CARRIER_ANY = 65537
    BUDDY_ANY = 131073
    INSTALL_IOS = 196609
    INSTALL_ANDROID = 196610
    MISSION_ANY = 262145
    MUSTBUY_ANY = 327681

    _VALUES_TO_NAMES = {
        0: "NO_EVENT",
        65537: "CARRIER_ANY",
        131073: "BUDDY_ANY",
        196609: "INSTALL_IOS",
        196610: "INSTALL_ANDROID",
        262145: "MISSION_ANY",
        327681: "MUSTBUY_ANY",
    }

    _NAMES_TO_VALUES = {
        "NO_EVENT": 0,
        "CARRIER_ANY": 65537,
        "BUDDY_ANY": 131073,
        "INSTALL_IOS": 196609,
        "INSTALL_ANDROID": 196610,
        "MISSION_ANY": 262145,
        "MUSTBUY_ANY": 327681,
    }


class ProfileAttribute(object):
    EMAIL = 1
    DISPLAY_NAME = 2
    PHONETIC_NAME = 4
    PICTURE = 8
    STATUS_MESSAGE = 16
    ALLOW_SEARCH_BY_USERID = 32
    ALLOW_SEARCH_BY_EMAIL = 64
    BUDDY_STATUS = 128
    ALL = 255

    _VALUES_TO_NAMES = {
        1: "EMAIL",
        2: "DISPLAY_NAME",
        4: "PHONETIC_NAME",
        8: "PICTURE",
        16: "STATUS_MESSAGE",
        32: "ALLOW_SEARCH_BY_USERID",
        64: "ALLOW_SEARCH_BY_EMAIL",
        128: "BUDDY_STATUS",
        255: "ALL",
    }

    _NAMES_TO_VALUES = {
        "EMAIL": 1,
        "DISPLAY_NAME": 2,
        "PHONETIC_NAME": 4,
        "PICTURE": 8,
        "STATUS_MESSAGE": 16,
        "ALLOW_SEARCH_BY_USERID": 32,
        "ALLOW_SEARCH_BY_EMAIL": 64,
        "BUDDY_STATUS": 128,
        "ALL": 255,
    }


class PublicType(object):
    HIDDEN = 0
    PUBLIC = 1000

    _VALUES_TO_NAMES = {
        0: "HIDDEN",
        1000: "PUBLIC",
    }

    _NAMES_TO_VALUES = {
        "HIDDEN": 0,
        "PUBLIC": 1000,
    }


class RedirectType(object):
    NONE = 0
    EXPIRE_SECOND = 1

    _VALUES_TO_NAMES = {
        0: "NONE",
        1: "EXPIRE_SECOND",
    }

    _NAMES_TO_VALUES = {
        "NONE": 0,
        "EXPIRE_SECOND": 1,
    }


class RegistrationType(object):
    PHONE = 0
    EMAIL_WAP = 1
    FACEBOOK = 2305
    SINA = 2306
    RENREN = 2307
    FEIXIN = 2308

    _VALUES_TO_NAMES = {
        0: "PHONE",
        1: "EMAIL_WAP",
        2305: "FACEBOOK",
        2306: "SINA",
        2307: "RENREN",
        2308: "FEIXIN",
    }

    _NAMES_TO_VALUES = {
        "PHONE": 0,
        "EMAIL_WAP": 1,
        "FACEBOOK": 2305,
        "SINA": 2306,
        "RENREN": 2307,
        "FEIXIN": 2308,
    }


class SettingsAttribute(object):
    NOTIFICATION_ENABLE = 1
    NOTIFICATION_MUTE_EXPIRATION = 2
    NOTIFICATION_NEW_MESSAGE = 4
    NOTIFICATION_GROUP_INVITATION = 8
    NOTIFICATION_SHOW_MESSAGE = 16
    NOTIFICATION_INCOMING_CALL = 32
    PRIVACY_SYNC_CONTACTS = 64
    PRIVACY_SEARCH_BY_PHONE_NUMBER = 128
    NOTIFICATION_SOUND_MESSAGE = 256
    NOTIFICATION_SOUND_GROUP = 512
    CONTACT_MY_TICKET = 1024
    IDENTITY_PROVIDER = 2048
    IDENTITY_IDENTIFIER = 4096
    PRIVACY_SEARCH_BY_USERID = 8192
    PRIVACY_SEARCH_BY_EMAIL = 16384
    PREFERENCE_LOCALE = 32768
    NOTIFICATION_DISABLED_WITH_SUB = 65536
    SNS_ACCOUNT = 524288
    PHONE_REGISTRATION = 1048576
    PRIVACY_ALLOW_SECONDARY_DEVICE_LOGIN = 2097152
    CUSTOM_MODE = 4194304
    PRIVACY_PROFILE_IMAGE_POST_TO_MYHOME = 8388608
    EMAIL_CONFIRMATION_STATUS = 16777216
    PRIVACY_RECV_MESSAGES_FROM_NOT_FRIEND = 33554432
    ALL = 2147483647

    _VALUES_TO_NAMES = {
        1: "NOTIFICATION_ENABLE",
        2: "NOTIFICATION_MUTE_EXPIRATION",
        4: "NOTIFICATION_NEW_MESSAGE",
        8: "NOTIFICATION_GROUP_INVITATION",
        16: "NOTIFICATION_SHOW_MESSAGE",
        32: "NOTIFICATION_INCOMING_CALL",
        64: "PRIVACY_SYNC_CONTACTS",
        128: "PRIVACY_SEARCH_BY_PHONE_NUMBER",
        256: "NOTIFICATION_SOUND_MESSAGE",
        512: "NOTIFICATION_SOUND_GROUP",
        1024: "CONTACT_MY_TICKET",
        2048: "IDENTITY_PROVIDER",
        4096: "IDENTITY_IDENTIFIER",
        8192: "PRIVACY_SEARCH_BY_USERID",
        16384: "PRIVACY_SEARCH_BY_EMAIL",
        32768: "PREFERENCE_LOCALE",
        65536: "NOTIFICATION_DISABLED_WITH_SUB",
        524288: "SNS_ACCOUNT",
        1048576: "PHONE_REGISTRATION",
        2097152: "PRIVACY_ALLOW_SECONDARY_DEVICE_LOGIN",
        4194304: "CUSTOM_MODE",
        8388608: "PRIVACY_PROFILE_IMAGE_POST_TO_MYHOME",
        16777216: "EMAIL_CONFIRMATION_STATUS",
        33554432: "PRIVACY_RECV_MESSAGES_FROM_NOT_FRIEND",
        2147483647: "ALL",
    }

    _NAMES_TO_VALUES = {
        "NOTIFICATION_ENABLE": 1,
        "NOTIFICATION_MUTE_EXPIRATION": 2,
        "NOTIFICATION_NEW_MESSAGE": 4,
        "NOTIFICATION_GROUP_INVITATION": 8,
        "NOTIFICATION_SHOW_MESSAGE": 16,
        "NOTIFICATION_INCOMING_CALL": 32,
        "PRIVACY_SYNC_CONTACTS": 64,
        "PRIVACY_SEARCH_BY_PHONE_NUMBER": 128,
        "NOTIFICATION_SOUND_MESSAGE": 256,
        "NOTIFICATION_SOUND_GROUP": 512,
        "CONTACT_MY_TICKET": 1024,
        "IDENTITY_PROVIDER": 2048,
        "IDENTITY_IDENTIFIER": 4096,
        "PRIVACY_SEARCH_BY_USERID": 8192,
        "PRIVACY_SEARCH_BY_EMAIL": 16384,
        "PREFERENCE_LOCALE": 32768,
        "NOTIFICATION_DISABLED_WITH_SUB": 65536,
        "SNS_ACCOUNT": 524288,
        "PHONE_REGISTRATION": 1048576,
        "PRIVACY_ALLOW_SECONDARY_DEVICE_LOGIN": 2097152,
        "CUSTOM_MODE": 4194304,
        "PRIVACY_PROFILE_IMAGE_POST_TO_MYHOME": 8388608,
        "EMAIL_CONFIRMATION_STATUS": 16777216,
        "PRIVACY_RECV_MESSAGES_FROM_NOT_FRIEND": 33554432,
        "ALL": 2147483647,
    }


class SnsIdType(object):
    FACEBOOK = 1
    SINA = 2
    RENREN = 3
    FEIXIN = 4

    _VALUES_TO_NAMES = {
        1: "FACEBOOK",
        2: "SINA",
        3: "RENREN",
        4: "FEIXIN",
    }

    _NAMES_TO_VALUES = {
        "FACEBOOK": 1,
        "SINA": 2,
        "RENREN": 3,
        "FEIXIN": 4,
    }


class SpammerReason(object):
    OTHER = 0
    ADVERTISING = 1
    GENDER_HARASSMENT = 2
    HARASSMENT = 3

    _VALUES_TO_NAMES = {
        0: "OTHER",
        1: "ADVERTISING",
        2: "GENDER_HARASSMENT",
        3: "HARASSMENT",
    }

    _NAMES_TO_VALUES = {
        "OTHER": 0,
        "ADVERTISING": 1,
        "GENDER_HARASSMENT": 2,
        "HARASSMENT": 3,
    }


class SyncActionType(object):
    SYNC = 0
    REPORT = 1

    _VALUES_TO_NAMES = {
        0: "SYNC",
        1: "REPORT",
    }

    _NAMES_TO_VALUES = {
        "SYNC": 0,
        "REPORT": 1,
    }


class SyncCategory(object):
    PROFILE = 0
    SETTINGS = 1
    OPS = 2
    CONTACT = 3
    RECOMMEND = 4
    BLOCK = 5
    GROUP = 6
    ROOM = 7
    NOTIFICATION = 8

    _VALUES_TO_NAMES = {
        0: "PROFILE",
        1: "SETTINGS",
        2: "OPS",
        3: "CONTACT",
        4: "RECOMMEND",
        5: "BLOCK",
        6: "GROUP",
        7: "ROOM",
        8: "NOTIFICATION",
    }

    _NAMES_TO_VALUES = {
        "PROFILE": 0,
        "SETTINGS": 1,
        "OPS": 2,
        "CONTACT": 3,
        "RECOMMEND": 4,
        "BLOCK": 5,
        "GROUP": 6,
        "ROOM": 7,
        "NOTIFICATION": 8,
    }


class TMessageBoxStatus(object):
    ACTIVATED = 1
    UNREAD = 2

    _VALUES_TO_NAMES = {
        1: "ACTIVATED",
        2: "UNREAD",
    }

    _NAMES_TO_VALUES = {
        "ACTIVATED": 1,
        "UNREAD": 2,
    }


class UniversalNotificationServiceErrorCode(object):
    INTERNAL_ERROR = 0
    INVALID_KEY = 1
    ILLEGAL_ARGUMENT = 2
    TOO_MANY_REQUEST = 3
    AUTHENTICATION_FAILED = 4
    NO_WRITE_PERMISSION = 5

    _VALUES_TO_NAMES = {
        0: "INTERNAL_ERROR",
        1: "INVALID_KEY",
        2: "ILLEGAL_ARGUMENT",
        3: "TOO_MANY_REQUEST",
        4: "AUTHENTICATION_FAILED",
        5: "NO_WRITE_PERMISSION",
    }

    _NAMES_TO_VALUES = {
        "INTERNAL_ERROR": 0,
        "INVALID_KEY": 1,
        "ILLEGAL_ARGUMENT": 2,
        "TOO_MANY_REQUEST": 3,
        "AUTHENTICATION_FAILED": 4,
        "NO_WRITE_PERMISSION": 5,
    }


class UnregistrationReason(object):
    UNREGISTRATION_REASON_UNREGISTER_USER = 1
    UNREGISTRATION_REASON_UNBIND_DEVICE = 2

    _VALUES_TO_NAMES = {
        1: "UNREGISTRATION_REASON_UNREGISTER_USER",
        2: "UNREGISTRATION_REASON_UNBIND_DEVICE",
    }

    _NAMES_TO_VALUES = {
        "UNREGISTRATION_REASON_UNREGISTER_USER": 1,
        "UNREGISTRATION_REASON_UNBIND_DEVICE": 2,
    }


class UserAgeType(object):
    OVER = 1
    UNDER = 2
    UNDEFINED = 3

    _VALUES_TO_NAMES = {
        1: "OVER",
        2: "UNDER",
        3: "UNDEFINED",
    }

    _NAMES_TO_VALUES = {
        "OVER": 1,
        "UNDER": 2,
        "UNDEFINED": 3,
    }


class VerificationMethod(object):
    NO_AVAILABLE = 0
    PIN_VIA_SMS = 1
    CALLERID_INDIGO = 2
    PIN_VIA_TTS = 4
    SKIP = 10

    _VALUES_TO_NAMES = {
        0: "NO_AVAILABLE",
        1: "PIN_VIA_SMS",
        2: "CALLERID_INDIGO",
        4: "PIN_VIA_TTS",
        10: "SKIP",
    }

    _NAMES_TO_VALUES = {
        "NO_AVAILABLE": 0,
        "PIN_VIA_SMS": 1,
        "CALLERID_INDIGO": 2,
        "PIN_VIA_TTS": 4,
        "SKIP": 10,
    }


class VerificationResult(object):
    FAILED = 0
    OK_NOT_REGISTERED_YET = 1
    OK_REGISTERED_WITH_SAME_DEVICE = 2
    OK_REGISTERED_WITH_ANOTHER_DEVICE = 3

    _VALUES_TO_NAMES = {
        0: "FAILED",
        1: "OK_NOT_REGISTERED_YET",
        2: "OK_REGISTERED_WITH_SAME_DEVICE",
        3: "OK_REGISTERED_WITH_ANOTHER_DEVICE",
    }

    _NAMES_TO_VALUES = {
        "FAILED": 0,
        "OK_NOT_REGISTERED_YET": 1,
        "OK_REGISTERED_WITH_SAME_DEVICE": 2,
        "OK_REGISTERED_WITH_ANOTHER_DEVICE": 3,
    }


class WapInvitationType(object):
    REGISTRATION = 1
    CHAT = 2

    _VALUES_TO_NAMES = {
        1: "REGISTRATION",
        2: "CHAT",
    }

    _NAMES_TO_VALUES = {
        "REGISTRATION": 1,
        "CHAT": 2,
    }


class AgeCheckDocomoResult(object):
    """
    Attributes:
     - authUrl
     - userAgeType
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'authUrl', 'UTF8', None, ),  # 1
        (2, TType.I32, 'userAgeType', None, None, ),  # 2
    )

    def __init__(self, authUrl=None, userAgeType=None,):
        self.authUrl = authUrl
        self.userAgeType = userAgeType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.authUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.userAgeType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AgeCheckDocomoResult')
        if self.authUrl is not None:
            oprot.writeFieldBegin('authUrl', TType.STRING, 1)
            oprot.writeString(self.authUrl.encode('utf-8') if sys.version_info[0] == 2 else self.authUrl)
            oprot.writeFieldEnd()
        if self.userAgeType is not None:
            oprot.writeFieldBegin('userAgeType', TType.I32, 2)
            oprot.writeI32(self.userAgeType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AgeCheckRequestResult(object):
    """
    Attributes:
     - authUrl
     - sessionId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'authUrl', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'sessionId', 'UTF8', None, ),  # 2
    )

    def __init__(self, authUrl=None, sessionId=None,):
        self.authUrl = authUrl
        self.sessionId = sessionId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.authUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.sessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AgeCheckRequestResult')
        if self.authUrl is not None:
            oprot.writeFieldBegin('authUrl', TType.STRING, 1)
            oprot.writeString(self.authUrl.encode('utf-8') if sys.version_info[0] == 2 else self.authUrl)
            oprot.writeFieldEnd()
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.STRING, 2)
            oprot.writeString(self.sessionId.encode('utf-8') if sys.version_info[0] == 2 else self.sessionId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Announcement(object):
    """
    Attributes:
     - index
     - forceUpdate
     - title
     - text
     - createdTime
     - pictureUrl
     - thumbnailUrl
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'index', None, None, ),  # 1
        None,  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.BOOL, 'forceUpdate', None, None, ),  # 10
        (11, TType.STRING, 'title', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'text', 'UTF8', None, ),  # 12
        (13, TType.I64, 'createdTime', None, None, ),  # 13
        (14, TType.STRING, 'pictureUrl', 'UTF8', None, ),  # 14
        (15, TType.STRING, 'thumbnailUrl', 'UTF8', None, ),  # 15
    )

    def __init__(self, index=None, forceUpdate=None, title=None, text=None, createdTime=None, pictureUrl=None, thumbnailUrl=None,):
        self.index = index
        self.forceUpdate = forceUpdate
        self.title = title
        self.text = text
        self.createdTime = createdTime
        self.pictureUrl = pictureUrl
        self.thumbnailUrl = thumbnailUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.BOOL:
                    self.forceUpdate = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.pictureUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Announcement')
        if self.index is not None:
            oprot.writeFieldBegin('index', TType.I32, 1)
            oprot.writeI32(self.index)
            oprot.writeFieldEnd()
        if self.forceUpdate is not None:
            oprot.writeFieldBegin('forceUpdate', TType.BOOL, 10)
            oprot.writeBool(self.forceUpdate)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 11)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 12)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 13)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.pictureUrl is not None:
            oprot.writeFieldBegin('pictureUrl', TType.STRING, 14)
            oprot.writeString(self.pictureUrl.encode('utf-8') if sys.version_info[0] == 2 else self.pictureUrl)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 15)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelProvider(object):
    """
    Attributes:
     - name
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    )

    def __init__(self, name=None,):
        self.name = name

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelProvider')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelInfo(object):
    """
    Attributes:
     - channelId
     - name
     - entryPageUrl
     - descriptionText
     - provider
     - publicType
     - iconImage
     - permissions
     - iconThumbnailImage
     - channelConfigurations
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
        None,  # 2
        (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'entryPageUrl', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'descriptionText', 'UTF8', None, ),  # 5
        (6, TType.STRUCT, 'provider', (ChannelProvider, ChannelProvider.thrift_spec), None, ),  # 6
        (7, TType.I32, 'publicType', None, None, ),  # 7
        (8, TType.STRING, 'iconImage', 'UTF8', None, ),  # 8
        (9, TType.LIST, 'permissions', (TType.STRING, 'UTF8', False), None, ),  # 9
        None,  # 10
        (11, TType.STRING, 'iconThumbnailImage', 'UTF8', None, ),  # 11
        (12, TType.LIST, 'channelConfigurations', (TType.I32, None, False), None, ),  # 12
    )

    def __init__(self, channelId=None, name=None, entryPageUrl=None, descriptionText=None, provider=None, publicType=None, iconImage=None, permissions=None, iconThumbnailImage=None, channelConfigurations=None,):
        self.channelId = channelId
        self.name = name
        self.entryPageUrl = entryPageUrl
        self.descriptionText = descriptionText
        self.provider = provider
        self.publicType = publicType
        self.iconImage = iconImage
        self.permissions = permissions
        self.iconThumbnailImage = iconThumbnailImage
        self.channelConfigurations = channelConfigurations

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.entryPageUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.descriptionText = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.provider = ChannelProvider()
                    self.provider.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.publicType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.iconImage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.permissions = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.permissions.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.iconThumbnailImage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.LIST:
                    self.channelConfigurations = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readI32()
                        self.channelConfigurations.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelInfo')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.entryPageUrl is not None:
            oprot.writeFieldBegin('entryPageUrl', TType.STRING, 4)
            oprot.writeString(self.entryPageUrl.encode('utf-8') if sys.version_info[0] == 2 else self.entryPageUrl)
            oprot.writeFieldEnd()
        if self.descriptionText is not None:
            oprot.writeFieldBegin('descriptionText', TType.STRING, 5)
            oprot.writeString(self.descriptionText.encode('utf-8') if sys.version_info[0] == 2 else self.descriptionText)
            oprot.writeFieldEnd()
        if self.provider is not None:
            oprot.writeFieldBegin('provider', TType.STRUCT, 6)
            self.provider.write(oprot)
            oprot.writeFieldEnd()
        if self.publicType is not None:
            oprot.writeFieldBegin('publicType', TType.I32, 7)
            oprot.writeI32(self.publicType)
            oprot.writeFieldEnd()
        if self.iconImage is not None:
            oprot.writeFieldBegin('iconImage', TType.STRING, 8)
            oprot.writeString(self.iconImage.encode('utf-8') if sys.version_info[0] == 2 else self.iconImage)
            oprot.writeFieldEnd()
        if self.permissions is not None:
            oprot.writeFieldBegin('permissions', TType.LIST, 9)
            oprot.writeListBegin(TType.STRING, len(self.permissions))
            for iter12 in self.permissions:
                oprot.writeString(iter12.encode('utf-8') if sys.version_info[0] == 2 else iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.iconThumbnailImage is not None:
            oprot.writeFieldBegin('iconThumbnailImage', TType.STRING, 11)
            oprot.writeString(self.iconThumbnailImage.encode('utf-8') if sys.version_info[0] == 2 else self.iconThumbnailImage)
            oprot.writeFieldEnd()
        if self.channelConfigurations is not None:
            oprot.writeFieldBegin('channelConfigurations', TType.LIST, 12)
            oprot.writeListBegin(TType.I32, len(self.channelConfigurations))
            for iter13 in self.channelConfigurations:
                oprot.writeI32(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ApprovedChannelInfo(object):
    """
    Attributes:
     - channelInfo
     - approvedAt
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'channelInfo', (ChannelInfo, ChannelInfo.thrift_spec), None, ),  # 1
        (2, TType.I64, 'approvedAt', None, None, ),  # 2
    )

    def __init__(self, channelInfo=None, approvedAt=None,):
        self.channelInfo = channelInfo
        self.approvedAt = approvedAt

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.channelInfo = ChannelInfo()
                    self.channelInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.approvedAt = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ApprovedChannelInfo')
        if self.channelInfo is not None:
            oprot.writeFieldBegin('channelInfo', TType.STRUCT, 1)
            self.channelInfo.write(oprot)
            oprot.writeFieldEnd()
        if self.approvedAt is not None:
            oprot.writeFieldBegin('approvedAt', TType.I64, 2)
            oprot.writeI64(self.approvedAt)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ApprovedChannelInfos(object):
    """
    Attributes:
     - approvedChannelInfos
     - revision
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'approvedChannelInfos', (TType.STRUCT, (ApprovedChannelInfo, ApprovedChannelInfo.thrift_spec), False), None, ),  # 1
        (2, TType.I64, 'revision', None, None, ),  # 2
    )

    def __init__(self, approvedChannelInfos=None, revision=None,):
        self.approvedChannelInfos = approvedChannelInfos
        self.revision = revision

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.approvedChannelInfos = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = ApprovedChannelInfo()
                        _elem19.read(iprot)
                        self.approvedChannelInfos.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ApprovedChannelInfos')
        if self.approvedChannelInfos is not None:
            oprot.writeFieldBegin('approvedChannelInfos', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.approvedChannelInfos))
            for iter20 in self.approvedChannelInfos:
                iter20.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 2)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthQrcode(object):
    """
    Attributes:
     - qrcode
     - verifier
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'qrcode', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'verifier', 'UTF8', None, ),  # 2
    )

    def __init__(self, qrcode=None, verifier=None,):
        self.qrcode = qrcode
        self.verifier = verifier

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.qrcode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AuthQrcode')
        if self.qrcode is not None:
            oprot.writeFieldBegin('qrcode', TType.STRING, 1)
            oprot.writeString(self.qrcode.encode('utf-8') if sys.version_info[0] == 2 else self.qrcode)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 2)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyBanner(object):
    """
    Attributes:
     - buddyBannerLinkType
     - buddyBannerLink
     - buddyBannerImageUrl
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'buddyBannerLinkType', None, None, ),  # 1
        (2, TType.STRING, 'buddyBannerLink', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'buddyBannerImageUrl', 'UTF8', None, ),  # 3
    )

    def __init__(self, buddyBannerLinkType=None, buddyBannerLink=None, buddyBannerImageUrl=None,):
        self.buddyBannerLinkType = buddyBannerLinkType
        self.buddyBannerLink = buddyBannerLink
        self.buddyBannerImageUrl = buddyBannerImageUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.buddyBannerLinkType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.buddyBannerLink = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.buddyBannerImageUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyBanner')
        if self.buddyBannerLinkType is not None:
            oprot.writeFieldBegin('buddyBannerLinkType', TType.I32, 1)
            oprot.writeI32(self.buddyBannerLinkType)
            oprot.writeFieldEnd()
        if self.buddyBannerLink is not None:
            oprot.writeFieldBegin('buddyBannerLink', TType.STRING, 2)
            oprot.writeString(self.buddyBannerLink.encode('utf-8') if sys.version_info[0] == 2 else self.buddyBannerLink)
            oprot.writeFieldEnd()
        if self.buddyBannerImageUrl is not None:
            oprot.writeFieldBegin('buddyBannerImageUrl', TType.STRING, 3)
            oprot.writeString(self.buddyBannerImageUrl.encode('utf-8') if sys.version_info[0] == 2 else self.buddyBannerImageUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyDetail(object):
    """
    Attributes:
     - mid
     - memberCount
     - onAir
     - businessAccount
     - addable
     - acceptableContentTypes
     - capableMyhome
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.I64, 'memberCount', None, None, ),  # 2
        (3, TType.BOOL, 'onAir', None, None, ),  # 3
        (4, TType.BOOL, 'businessAccount', None, None, ),  # 4
        (5, TType.BOOL, 'addable', None, None, ),  # 5
        (6, TType.SET, 'acceptableContentTypes', (TType.I32, None, False), None, ),  # 6
        (7, TType.BOOL, 'capableMyhome', None, None, ),  # 7
    )

    def __init__(self, mid=None, memberCount=None, onAir=None, businessAccount=None, addable=None, acceptableContentTypes=None, capableMyhome=None,):
        self.mid = mid
        self.memberCount = memberCount
        self.onAir = onAir
        self.businessAccount = businessAccount
        self.addable = addable
        self.acceptableContentTypes = acceptableContentTypes
        self.capableMyhome = capableMyhome

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.memberCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.onAir = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.businessAccount = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.addable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.SET:
                    self.acceptableContentTypes = set()
                    (_etype24, _size21) = iprot.readSetBegin()
                    for _i25 in range(_size21):
                        _elem26 = iprot.readI32()
                        self.acceptableContentTypes.add(_elem26)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.capableMyhome = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyDetail')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.memberCount is not None:
            oprot.writeFieldBegin('memberCount', TType.I64, 2)
            oprot.writeI64(self.memberCount)
            oprot.writeFieldEnd()
        if self.onAir is not None:
            oprot.writeFieldBegin('onAir', TType.BOOL, 3)
            oprot.writeBool(self.onAir)
            oprot.writeFieldEnd()
        if self.businessAccount is not None:
            oprot.writeFieldBegin('businessAccount', TType.BOOL, 4)
            oprot.writeBool(self.businessAccount)
            oprot.writeFieldEnd()
        if self.addable is not None:
            oprot.writeFieldBegin('addable', TType.BOOL, 5)
            oprot.writeBool(self.addable)
            oprot.writeFieldEnd()
        if self.acceptableContentTypes is not None:
            oprot.writeFieldBegin('acceptableContentTypes', TType.SET, 6)
            oprot.writeSetBegin(TType.I32, len(self.acceptableContentTypes))
            for iter27 in self.acceptableContentTypes:
                oprot.writeI32(iter27)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        if self.capableMyhome is not None:
            oprot.writeFieldBegin('capableMyhome', TType.BOOL, 7)
            oprot.writeBool(self.capableMyhome)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Contact(object):
    """
    Attributes:
     - mid
     - createdTime
     - type
     - status
     - relation
     - displayName
     - phoneticName
     - pictureStatus
     - thumbnailUrl
     - statusMessage
     - displayNameOverridden
     - favoriteTime
     - capableVoiceCall
     - capableVideoCall
     - capableMyhome
     - capableBuddy
     - attributes
     - settings
     - picturePath
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.I32, 'type', None, None, ),  # 10
        (11, TType.I32, 'status', None, None, ),  # 11
        None,  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        (21, TType.I32, 'relation', None, None, ),  # 21
        (22, TType.STRING, 'displayName', 'UTF8', None, ),  # 22
        (23, TType.STRING, 'phoneticName', 'UTF8', None, ),  # 23
        (24, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 24
        (25, TType.STRING, 'thumbnailUrl', 'UTF8', None, ),  # 25
        (26, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 26
        (27, TType.STRING, 'displayNameOverridden', 'UTF8', None, ),  # 27
        (28, TType.I64, 'favoriteTime', None, None, ),  # 28
        None,  # 29
        None,  # 30
        (31, TType.BOOL, 'capableVoiceCall', None, None, ),  # 31
        (32, TType.BOOL, 'capableVideoCall', None, None, ),  # 32
        (33, TType.BOOL, 'capableMyhome', None, None, ),  # 33
        (34, TType.BOOL, 'capableBuddy', None, None, ),  # 34
        (35, TType.I32, 'attributes', None, None, ),  # 35
        (36, TType.I64, 'settings', None, None, ),  # 36
        (37, TType.STRING, 'picturePath', 'UTF8', None, ),  # 37
    )

    def __init__(self, mid=None, createdTime=None, type=None, status=None, relation=None, displayName=None, phoneticName=None, pictureStatus=None, thumbnailUrl=None, statusMessage=None, displayNameOverridden=None, favoriteTime=None, capableVoiceCall=None, capableVideoCall=None, capableMyhome=None, capableBuddy=None, attributes=None, settings=None, picturePath=None,):
        self.mid = mid
        self.createdTime = createdTime
        self.type = type
        self.status = status
        self.relation = relation
        self.displayName = displayName
        self.phoneticName = phoneticName
        self.pictureStatus = pictureStatus
        self.thumbnailUrl = thumbnailUrl
        self.statusMessage = statusMessage
        self.displayNameOverridden = displayNameOverridden
        self.favoriteTime = favoriteTime
        self.capableVoiceCall = capableVoiceCall
        self.capableVideoCall = capableVideoCall
        self.capableMyhome = capableMyhome
        self.capableBuddy = capableBuddy
        self.attributes = attributes
        self.settings = settings
        self.picturePath = picturePath

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.relation = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.phoneticName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.STRING:
                    self.displayNameOverridden = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.I64:
                    self.favoriteTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.capableVoiceCall = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 32:
                if ftype == TType.BOOL:
                    self.capableVideoCall = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 33:
                if ftype == TType.BOOL:
                    self.capableMyhome = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 34:
                if ftype == TType.BOOL:
                    self.capableBuddy = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 35:
                if ftype == TType.I32:
                    self.attributes = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 36:
                if ftype == TType.I64:
                    self.settings = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 37:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Contact')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 10)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 11)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.relation is not None:
            oprot.writeFieldBegin('relation', TType.I32, 21)
            oprot.writeI32(self.relation)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 22)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.phoneticName is not None:
            oprot.writeFieldBegin('phoneticName', TType.STRING, 23)
            oprot.writeString(self.phoneticName.encode('utf-8') if sys.version_info[0] == 2 else self.phoneticName)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 24)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 25)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 26)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.displayNameOverridden is not None:
            oprot.writeFieldBegin('displayNameOverridden', TType.STRING, 27)
            oprot.writeString(self.displayNameOverridden.encode('utf-8') if sys.version_info[0] == 2 else self.displayNameOverridden)
            oprot.writeFieldEnd()
        if self.favoriteTime is not None:
            oprot.writeFieldBegin('favoriteTime', TType.I64, 28)
            oprot.writeI64(self.favoriteTime)
            oprot.writeFieldEnd()
        if self.capableVoiceCall is not None:
            oprot.writeFieldBegin('capableVoiceCall', TType.BOOL, 31)
            oprot.writeBool(self.capableVoiceCall)
            oprot.writeFieldEnd()
        if self.capableVideoCall is not None:
            oprot.writeFieldBegin('capableVideoCall', TType.BOOL, 32)
            oprot.writeBool(self.capableVideoCall)
            oprot.writeFieldEnd()
        if self.capableMyhome is not None:
            oprot.writeFieldBegin('capableMyhome', TType.BOOL, 33)
            oprot.writeBool(self.capableMyhome)
            oprot.writeFieldEnd()
        if self.capableBuddy is not None:
            oprot.writeFieldBegin('capableBuddy', TType.BOOL, 34)
            oprot.writeBool(self.capableBuddy)
            oprot.writeFieldEnd()
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.I32, 35)
            oprot.writeI32(self.attributes)
            oprot.writeFieldEnd()
        if self.settings is not None:
            oprot.writeFieldBegin('settings', TType.I64, 36)
            oprot.writeI64(self.settings)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 37)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyList(object):
    """
    Attributes:
     - classification
     - displayName
     - totalBuddyCount
     - popularContacts
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'classification', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'displayName', 'UTF8', None, ),  # 2
        (3, TType.I32, 'totalBuddyCount', None, None, ),  # 3
        (4, TType.LIST, 'popularContacts', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 4
    )

    def __init__(self, classification=None, displayName=None, totalBuddyCount=None, popularContacts=None,):
        self.classification = classification
        self.displayName = displayName
        self.totalBuddyCount = totalBuddyCount
        self.popularContacts = popularContacts

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.classification = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.totalBuddyCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.popularContacts = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = Contact()
                        _elem33.read(iprot)
                        self.popularContacts.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyList')
        if self.classification is not None:
            oprot.writeFieldBegin('classification', TType.STRING, 1)
            oprot.writeString(self.classification.encode('utf-8') if sys.version_info[0] == 2 else self.classification)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 2)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.totalBuddyCount is not None:
            oprot.writeFieldBegin('totalBuddyCount', TType.I32, 3)
            oprot.writeI32(self.totalBuddyCount)
            oprot.writeFieldEnd()
        if self.popularContacts is not None:
            oprot.writeFieldBegin('popularContacts', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.popularContacts))
            for iter34 in self.popularContacts:
                iter34.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Location(object):
    """
    Attributes:
     - title
     - address
     - latitude
     - longitude
     - phone
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'title', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'address', 'UTF8', None, ),  # 2
        (3, TType.DOUBLE, 'latitude', None, None, ),  # 3
        (4, TType.DOUBLE, 'longitude', None, None, ),  # 4
        (5, TType.STRING, 'phone', 'UTF8', None, ),  # 5
    )

    def __init__(self, title=None, address=None, latitude=None, longitude=None, phone=None,):
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.phone = phone

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.address = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.latitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.longitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.phone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Location')
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 1)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.address is not None:
            oprot.writeFieldBegin('address', TType.STRING, 2)
            oprot.writeString(self.address.encode('utf-8') if sys.version_info[0] == 2 else self.address)
            oprot.writeFieldEnd()
        if self.latitude is not None:
            oprot.writeFieldBegin('latitude', TType.DOUBLE, 3)
            oprot.writeDouble(self.latitude)
            oprot.writeFieldEnd()
        if self.longitude is not None:
            oprot.writeFieldBegin('longitude', TType.DOUBLE, 4)
            oprot.writeDouble(self.longitude)
            oprot.writeFieldEnd()
        if self.phone is not None:
            oprot.writeFieldBegin('phone', TType.STRING, 5)
            oprot.writeString(self.phone.encode('utf-8') if sys.version_info[0] == 2 else self.phone)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyMessageRequest(object):
    """
    Attributes:
     - contentType
     - text
     - location
     - content
     - contentMetadata
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'contentType', None, None, ),  # 1
        (2, TType.STRING, 'text', 'UTF8', None, ),  # 2
        (3, TType.STRUCT, 'location', (Location, Location.thrift_spec), None, ),  # 3
        (4, TType.STRING, 'content', 'BINARY', None, ),  # 4
        (5, TType.MAP, 'contentMetadata', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 5
    )

    def __init__(self, contentType=None, text=None, location=None, content=None, contentMetadata=None,):
        self.contentType = contentType
        self.text = text
        self.location = location
        self.content = content
        self.contentMetadata = contentMetadata

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.contentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.location = Location()
                    self.location.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.MAP:
                    self.contentMetadata = {}
                    (_ktype36, _vtype37, _size35) = iprot.readMapBegin()
                    for _i39 in range(_size35):
                        _key40 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val41 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.contentMetadata[_key40] = _val41
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyMessageRequest')
        if self.contentType is not None:
            oprot.writeFieldBegin('contentType', TType.I32, 1)
            oprot.writeI32(self.contentType)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 2)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.location is not None:
            oprot.writeFieldBegin('location', TType.STRUCT, 3)
            self.location.write(oprot)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 4)
            oprot.writeBinary(self.content)
            oprot.writeFieldEnd()
        if self.contentMetadata is not None:
            oprot.writeFieldBegin('contentMetadata', TType.MAP, 5)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.contentMetadata))
            for kiter42, viter43 in self.contentMetadata.items():
                oprot.writeString(kiter42.encode('utf-8') if sys.version_info[0] == 2 else kiter42)
                oprot.writeString(viter43.encode('utf-8') if sys.version_info[0] == 2 else viter43)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyOnAirUrls(object):
    """
    Attributes:
     - hls
     - smoothStreaming
    """

    thrift_spec = (
        None,  # 0
        (1, TType.MAP, 'hls', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 1
        (2, TType.MAP, 'smoothStreaming', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
    )

    def __init__(self, hls=None, smoothStreaming=None,):
        self.hls = hls
        self.smoothStreaming = smoothStreaming

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.hls = {}
                    (_ktype45, _vtype46, _size44) = iprot.readMapBegin()
                    for _i48 in range(_size44):
                        _key49 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val50 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.hls[_key49] = _val50
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.smoothStreaming = {}
                    (_ktype52, _vtype53, _size51) = iprot.readMapBegin()
                    for _i55 in range(_size51):
                        _key56 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val57 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.smoothStreaming[_key56] = _val57
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyOnAirUrls')
        if self.hls is not None:
            oprot.writeFieldBegin('hls', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.hls))
            for kiter58, viter59 in self.hls.items():
                oprot.writeString(kiter58.encode('utf-8') if sys.version_info[0] == 2 else kiter58)
                oprot.writeString(viter59.encode('utf-8') if sys.version_info[0] == 2 else viter59)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.smoothStreaming is not None:
            oprot.writeFieldBegin('smoothStreaming', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.smoothStreaming))
            for kiter60, viter61 in self.smoothStreaming.items():
                oprot.writeString(kiter60.encode('utf-8') if sys.version_info[0] == 2 else kiter60)
                oprot.writeString(viter61.encode('utf-8') if sys.version_info[0] == 2 else viter61)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyOnAir(object):
    """
    Attributes:
     - mid
     - freshnessLifetime
     - onAirId
     - onAir
     - text
     - viewerCount
     - targetCount
     - onAirType
     - onAirUrls
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        None,  # 2
        (3, TType.I64, 'freshnessLifetime', None, None, ),  # 3
        (4, TType.STRING, 'onAirId', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'onAir', None, None, ),  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.STRING, 'text', 'UTF8', None, ),  # 11
        (12, TType.I64, 'viewerCount', None, None, ),  # 12
        (13, TType.I64, 'targetCount', None, None, ),  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        None,  # 21
        None,  # 22
        None,  # 23
        None,  # 24
        None,  # 25
        None,  # 26
        None,  # 27
        None,  # 28
        None,  # 29
        None,  # 30
        (31, TType.I32, 'onAirType', None, None, ),  # 31
        (32, TType.STRUCT, 'onAirUrls', (BuddyOnAirUrls, BuddyOnAirUrls.thrift_spec), None, ),  # 32
    )

    def __init__(self, mid=None, freshnessLifetime=None, onAirId=None, onAir=None, text=None, viewerCount=None, targetCount=None, onAirType=None, onAirUrls=None,):
        self.mid = mid
        self.freshnessLifetime = freshnessLifetime
        self.onAirId = onAirId
        self.onAir = onAir
        self.text = text
        self.viewerCount = viewerCount
        self.targetCount = targetCount
        self.onAirType = onAirType
        self.onAirUrls = onAirUrls

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.freshnessLifetime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.onAirId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.onAir = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.viewerCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.targetCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.I32:
                    self.onAirType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 32:
                if ftype == TType.STRUCT:
                    self.onAirUrls = BuddyOnAirUrls()
                    self.onAirUrls.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyOnAir')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.freshnessLifetime is not None:
            oprot.writeFieldBegin('freshnessLifetime', TType.I64, 3)
            oprot.writeI64(self.freshnessLifetime)
            oprot.writeFieldEnd()
        if self.onAirId is not None:
            oprot.writeFieldBegin('onAirId', TType.STRING, 4)
            oprot.writeString(self.onAirId.encode('utf-8') if sys.version_info[0] == 2 else self.onAirId)
            oprot.writeFieldEnd()
        if self.onAir is not None:
            oprot.writeFieldBegin('onAir', TType.BOOL, 5)
            oprot.writeBool(self.onAir)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 11)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.viewerCount is not None:
            oprot.writeFieldBegin('viewerCount', TType.I64, 12)
            oprot.writeI64(self.viewerCount)
            oprot.writeFieldEnd()
        if self.targetCount is not None:
            oprot.writeFieldBegin('targetCount', TType.I64, 13)
            oprot.writeI64(self.targetCount)
            oprot.writeFieldEnd()
        if self.onAirType is not None:
            oprot.writeFieldBegin('onAirType', TType.I32, 31)
            oprot.writeI32(self.onAirType)
            oprot.writeFieldEnd()
        if self.onAirUrls is not None:
            oprot.writeFieldBegin('onAirUrls', TType.STRUCT, 32)
            self.onAirUrls.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyProfile(object):
    """
    Attributes:
     - buddyId
     - mid
     - searchId
     - displayName
     - statusMessage
     - contactCount
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'buddyId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'searchId', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'displayName', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.I64, 'contactCount', None, None, ),  # 11
    )

    def __init__(self, buddyId=None, mid=None, searchId=None, displayName=None, statusMessage=None, contactCount=None,):
        self.buddyId = buddyId
        self.mid = mid
        self.searchId = searchId
        self.displayName = displayName
        self.statusMessage = statusMessage
        self.contactCount = contactCount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.buddyId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.searchId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.contactCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddyProfile')
        if self.buddyId is not None:
            oprot.writeFieldBegin('buddyId', TType.STRING, 1)
            oprot.writeString(self.buddyId.encode('utf-8') if sys.version_info[0] == 2 else self.buddyId)
            oprot.writeFieldEnd()
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 2)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.searchId is not None:
            oprot.writeFieldBegin('searchId', TType.STRING, 3)
            oprot.writeString(self.searchId.encode('utf-8') if sys.version_info[0] == 2 else self.searchId)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 4)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 5)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.contactCount is not None:
            oprot.writeFieldBegin('contactCount', TType.I64, 11)
            oprot.writeI64(self.contactCount)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddySearchResult(object):
    """
    Attributes:
     - mid
     - displayName
     - pictureStatus
     - picturePath
     - statusMessage
     - businessAccount
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'displayName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'picturePath', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 5
        (6, TType.BOOL, 'businessAccount', None, None, ),  # 6
    )

    def __init__(self, mid=None, displayName=None, pictureStatus=None, picturePath=None, statusMessage=None, businessAccount=None,):
        self.mid = mid
        self.displayName = displayName
        self.pictureStatus = pictureStatus
        self.picturePath = picturePath
        self.statusMessage = statusMessage
        self.businessAccount = businessAccount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BOOL:
                    self.businessAccount = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BuddySearchResult')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 2)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 3)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 4)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 5)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.businessAccount is not None:
            oprot.writeFieldBegin('businessAccount', TType.BOOL, 6)
            oprot.writeBool(self.businessAccount)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelDomain(object):
    """
    Attributes:
     - host
     - removed
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'host', 'UTF8', None, ),  # 1
        (2, TType.BOOL, 'removed', None, None, ),  # 2
    )

    def __init__(self, host=None, removed=None,):
        self.host = host
        self.removed = removed

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.host = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.removed = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelDomain')
        if self.host is not None:
            oprot.writeFieldBegin('host', TType.STRING, 1)
            oprot.writeString(self.host.encode('utf-8') if sys.version_info[0] == 2 else self.host)
            oprot.writeFieldEnd()
        if self.removed is not None:
            oprot.writeFieldBegin('removed', TType.BOOL, 2)
            oprot.writeBool(self.removed)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelDomains(object):
    """
    Attributes:
     - channelDomains
     - revision
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'channelDomains', (TType.STRUCT, (ChannelDomain, ChannelDomain.thrift_spec), False), None, ),  # 1
        (2, TType.I64, 'revision', None, None, ),  # 2
    )

    def __init__(self, channelDomains=None, revision=None,):
        self.channelDomains = channelDomains
        self.revision = revision

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.channelDomains = []
                    (_etype65, _size62) = iprot.readListBegin()
                    for _i66 in range(_size62):
                        _elem67 = ChannelDomain()
                        _elem67.read(iprot)
                        self.channelDomains.append(_elem67)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelDomains')
        if self.channelDomains is not None:
            oprot.writeFieldBegin('channelDomains', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.channelDomains))
            for iter68 in self.channelDomains:
                iter68.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 2)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelException(TException):
    """
    Attributes:
     - code
     - reason
     - parameterMap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None, ),  # 1
        (2, TType.STRING, 'reason', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'parameterMap', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, code=None, reason=None, parameterMap=None,):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype70, _vtype71, _size69) = iprot.readMapBegin()
                    for _i73 in range(_size69):
                        _key74 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val75 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key74] = _val75
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 2)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter76, viter77 in self.parameterMap.items():
                oprot.writeString(kiter76.encode('utf-8') if sys.version_info[0] == 2 else kiter76)
                oprot.writeString(viter77.encode('utf-8') if sys.version_info[0] == 2 else viter77)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelInfos(object):
    """
    Attributes:
     - channelInfos
     - revision
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'channelInfos', (TType.STRUCT, (ChannelInfo, ChannelInfo.thrift_spec), False), None, ),  # 1
        (2, TType.I64, 'revision', None, None, ),  # 2
    )

    def __init__(self, channelInfos=None, revision=None,):
        self.channelInfos = channelInfos
        self.revision = revision

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.channelInfos = []
                    (_etype81, _size78) = iprot.readListBegin()
                    for _i82 in range(_size78):
                        _elem83 = ChannelInfo()
                        _elem83.read(iprot)
                        self.channelInfos.append(_elem83)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelInfos')
        if self.channelInfos is not None:
            oprot.writeFieldBegin('channelInfos', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.channelInfos))
            for iter84 in self.channelInfos:
                iter84.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 2)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelNotificationSetting(object):
    """
    Attributes:
     - channelId
     - name
     - notificationReceivable
     - messageReceivable
     - showDefault
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
        (3, TType.BOOL, 'notificationReceivable', None, None, ),  # 3
        (4, TType.BOOL, 'messageReceivable', None, None, ),  # 4
        (5, TType.BOOL, 'showDefault', None, None, ),  # 5
    )

    def __init__(self, channelId=None, name=None, notificationReceivable=None, messageReceivable=None, showDefault=None,):
        self.channelId = channelId
        self.name = name
        self.notificationReceivable = notificationReceivable
        self.messageReceivable = messageReceivable
        self.showDefault = showDefault

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.notificationReceivable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.messageReceivable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.showDefault = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelNotificationSetting')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.notificationReceivable is not None:
            oprot.writeFieldBegin('notificationReceivable', TType.BOOL, 3)
            oprot.writeBool(self.notificationReceivable)
            oprot.writeFieldEnd()
        if self.messageReceivable is not None:
            oprot.writeFieldBegin('messageReceivable', TType.BOOL, 4)
            oprot.writeBool(self.messageReceivable)
            oprot.writeFieldEnd()
        if self.showDefault is not None:
            oprot.writeFieldBegin('showDefault', TType.BOOL, 5)
            oprot.writeBool(self.showDefault)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelSyncDatas(object):
    """
    Attributes:
     - channelInfos
     - channelDomains
     - revision
     - expires
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'channelInfos', (TType.STRUCT, (ChannelInfo, ChannelInfo.thrift_spec), False), None, ),  # 1
        (2, TType.LIST, 'channelDomains', (TType.STRUCT, (ChannelDomain, ChannelDomain.thrift_spec), False), None, ),  # 2
        (3, TType.I64, 'revision', None, None, ),  # 3
        (4, TType.I64, 'expires', None, None, ),  # 4
    )

    def __init__(self, channelInfos=None, channelDomains=None, revision=None, expires=None,):
        self.channelInfos = channelInfos
        self.channelDomains = channelDomains
        self.revision = revision
        self.expires = expires

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.channelInfos = []
                    (_etype88, _size85) = iprot.readListBegin()
                    for _i89 in range(_size85):
                        _elem90 = ChannelInfo()
                        _elem90.read(iprot)
                        self.channelInfos.append(_elem90)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.channelDomains = []
                    (_etype94, _size91) = iprot.readListBegin()
                    for _i95 in range(_size91):
                        _elem96 = ChannelDomain()
                        _elem96.read(iprot)
                        self.channelDomains.append(_elem96)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.expires = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelSyncDatas')
        if self.channelInfos is not None:
            oprot.writeFieldBegin('channelInfos', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.channelInfos))
            for iter97 in self.channelInfos:
                iter97.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.channelDomains is not None:
            oprot.writeFieldBegin('channelDomains', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.channelDomains))
            for iter98 in self.channelDomains:
                iter98.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 3)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        if self.expires is not None:
            oprot.writeFieldBegin('expires', TType.I64, 4)
            oprot.writeI64(self.expires)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChannelToken(object):
    """
    Attributes:
     - token
     - obsToken
     - expiration
     - refreshToken
     - channelAccessToken
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'token', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'obsToken', 'UTF8', None, ),  # 2
        (3, TType.I64, 'expiration', None, None, ),  # 3
        (4, TType.STRING, 'refreshToken', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'channelAccessToken', 'UTF8', None, ),  # 5
    )

    def __init__(self, token=None, obsToken=None, expiration=None, refreshToken=None, channelAccessToken=None,):
        self.token = token
        self.obsToken = obsToken
        self.expiration = expiration
        self.refreshToken = refreshToken
        self.channelAccessToken = channelAccessToken

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.obsToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.expiration = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.refreshToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.channelAccessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ChannelToken')
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 1)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.obsToken is not None:
            oprot.writeFieldBegin('obsToken', TType.STRING, 2)
            oprot.writeString(self.obsToken.encode('utf-8') if sys.version_info[0] == 2 else self.obsToken)
            oprot.writeFieldEnd()
        if self.expiration is not None:
            oprot.writeFieldBegin('expiration', TType.I64, 3)
            oprot.writeI64(self.expiration)
            oprot.writeFieldEnd()
        if self.refreshToken is not None:
            oprot.writeFieldBegin('refreshToken', TType.STRING, 4)
            oprot.writeString(self.refreshToken.encode('utf-8') if sys.version_info[0] == 2 else self.refreshToken)
            oprot.writeFieldEnd()
        if self.channelAccessToken is not None:
            oprot.writeFieldBegin('channelAccessToken', TType.STRING, 5)
            oprot.writeString(self.channelAccessToken.encode('utf-8') if sys.version_info[0] == 2 else self.channelAccessToken)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Coin(object):
    """
    Attributes:
     - freeCoinBalance
     - payedCoinBalance
     - totalCoinBalance
     - rewardCoinBalance
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'freeCoinBalance', None, None, ),  # 1
        (2, TType.I32, 'payedCoinBalance', None, None, ),  # 2
        (3, TType.I32, 'totalCoinBalance', None, None, ),  # 3
        (4, TType.I32, 'rewardCoinBalance', None, None, ),  # 4
    )

    def __init__(self, freeCoinBalance=None, payedCoinBalance=None, totalCoinBalance=None, rewardCoinBalance=None,):
        self.freeCoinBalance = freeCoinBalance
        self.payedCoinBalance = payedCoinBalance
        self.totalCoinBalance = totalCoinBalance
        self.rewardCoinBalance = rewardCoinBalance

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.freeCoinBalance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.payedCoinBalance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.totalCoinBalance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.rewardCoinBalance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Coin')
        if self.freeCoinBalance is not None:
            oprot.writeFieldBegin('freeCoinBalance', TType.I32, 1)
            oprot.writeI32(self.freeCoinBalance)
            oprot.writeFieldEnd()
        if self.payedCoinBalance is not None:
            oprot.writeFieldBegin('payedCoinBalance', TType.I32, 2)
            oprot.writeI32(self.payedCoinBalance)
            oprot.writeFieldEnd()
        if self.totalCoinBalance is not None:
            oprot.writeFieldBegin('totalCoinBalance', TType.I32, 3)
            oprot.writeI32(self.totalCoinBalance)
            oprot.writeFieldEnd()
        if self.rewardCoinBalance is not None:
            oprot.writeFieldBegin('rewardCoinBalance', TType.I32, 4)
            oprot.writeI32(self.rewardCoinBalance)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinPayLoad(object):
    """
    Attributes:
     - payCoin
     - freeCoin
     - type
     - rewardCoin
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'payCoin', None, None, ),  # 1
        (2, TType.I32, 'freeCoin', None, None, ),  # 2
        (3, TType.I32, 'type', None, None, ),  # 3
        (4, TType.I32, 'rewardCoin', None, None, ),  # 4
    )

    def __init__(self, payCoin=None, freeCoin=None, type=None, rewardCoin=None,):
        self.payCoin = payCoin
        self.freeCoin = freeCoin
        self.type = type
        self.rewardCoin = rewardCoin

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.payCoin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.freeCoin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.rewardCoin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinPayLoad')
        if self.payCoin is not None:
            oprot.writeFieldBegin('payCoin', TType.I32, 1)
            oprot.writeI32(self.payCoin)
            oprot.writeFieldEnd()
        if self.freeCoin is not None:
            oprot.writeFieldBegin('freeCoin', TType.I32, 2)
            oprot.writeI32(self.freeCoin)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.rewardCoin is not None:
            oprot.writeFieldBegin('rewardCoin', TType.I32, 4)
            oprot.writeI32(self.rewardCoin)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinHistory(object):
    """
    Attributes:
     - payDate
     - coinBalance
     - coin
     - price
     - title
     - refund
     - paySeq
     - currency
     - currencySign
     - displayPrice
     - payload
     - channelId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'payDate', None, None, ),  # 1
        (2, TType.I32, 'coinBalance', None, None, ),  # 2
        (3, TType.I32, 'coin', None, None, ),  # 3
        (4, TType.STRING, 'price', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'title', 'UTF8', None, ),  # 5
        (6, TType.BOOL, 'refund', None, None, ),  # 6
        (7, TType.STRING, 'paySeq', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'currency', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'currencySign', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'displayPrice', 'UTF8', None, ),  # 10
        (11, TType.STRUCT, 'payload', (CoinPayLoad, CoinPayLoad.thrift_spec), None, ),  # 11
        (12, TType.STRING, 'channelId', 'UTF8', None, ),  # 12
    )

    def __init__(self, payDate=None, coinBalance=None, coin=None, price=None, title=None, refund=None, paySeq=None, currency=None, currencySign=None, displayPrice=None, payload=None, channelId=None,):
        self.payDate = payDate
        self.coinBalance = coinBalance
        self.coin = coin
        self.price = price
        self.title = title
        self.refund = refund
        self.paySeq = paySeq
        self.currency = currency
        self.currencySign = currencySign
        self.displayPrice = displayPrice
        self.payload = payload
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.payDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.coinBalance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.coin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BOOL:
                    self.refund = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.paySeq = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.currencySign = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.displayPrice = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.payload = CoinPayLoad()
                    self.payload.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinHistory')
        if self.payDate is not None:
            oprot.writeFieldBegin('payDate', TType.I64, 1)
            oprot.writeI64(self.payDate)
            oprot.writeFieldEnd()
        if self.coinBalance is not None:
            oprot.writeFieldBegin('coinBalance', TType.I32, 2)
            oprot.writeI32(self.coinBalance)
            oprot.writeFieldEnd()
        if self.coin is not None:
            oprot.writeFieldBegin('coin', TType.I32, 3)
            oprot.writeI32(self.coin)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 4)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 5)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.refund is not None:
            oprot.writeFieldBegin('refund', TType.BOOL, 6)
            oprot.writeBool(self.refund)
            oprot.writeFieldEnd()
        if self.paySeq is not None:
            oprot.writeFieldBegin('paySeq', TType.STRING, 7)
            oprot.writeString(self.paySeq.encode('utf-8') if sys.version_info[0] == 2 else self.paySeq)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 8)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.currencySign is not None:
            oprot.writeFieldBegin('currencySign', TType.STRING, 9)
            oprot.writeString(self.currencySign.encode('utf-8') if sys.version_info[0] == 2 else self.currencySign)
            oprot.writeFieldEnd()
        if self.displayPrice is not None:
            oprot.writeFieldBegin('displayPrice', TType.STRING, 10)
            oprot.writeString(self.displayPrice.encode('utf-8') if sys.version_info[0] == 2 else self.displayPrice)
            oprot.writeFieldEnd()
        if self.payload is not None:
            oprot.writeFieldBegin('payload', TType.STRUCT, 11)
            self.payload.write(oprot)
            oprot.writeFieldEnd()
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 12)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinHistoryCondition(object):
    """
    Attributes:
     - start
     - size
     - language
     - eddt
     - appStoreCode
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'start', None, None, ),  # 1
        (2, TType.I32, 'size', None, None, ),  # 2
        (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'eddt', 'UTF8', None, ),  # 4
        (5, TType.I32, 'appStoreCode', None, None, ),  # 5
    )

    def __init__(self, start=None, size=None, language=None, eddt=None, appStoreCode=None,):
        self.start = start
        self.size = size
        self.language = language
        self.eddt = eddt
        self.appStoreCode = appStoreCode

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.eddt = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinHistoryCondition')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 1)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 2)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.eddt is not None:
            oprot.writeFieldBegin('eddt', TType.STRING, 4)
            oprot.writeString(self.eddt.encode('utf-8') if sys.version_info[0] == 2 else self.eddt)
            oprot.writeFieldEnd()
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 5)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinHistoryResult(object):
    """
    Attributes:
     - historys
     - balance
     - hasNext
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'historys', (TType.STRUCT, (CoinHistory, CoinHistory.thrift_spec), False), None, ),  # 1
        (2, TType.STRUCT, 'balance', (Coin, Coin.thrift_spec), None, ),  # 2
        (3, TType.BOOL, 'hasNext', None, None, ),  # 3
    )

    def __init__(self, historys=None, balance=None, hasNext=None,):
        self.historys = historys
        self.balance = balance
        self.hasNext = hasNext

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.historys = []
                    (_etype102, _size99) = iprot.readListBegin()
                    for _i103 in range(_size99):
                        _elem104 = CoinHistory()
                        _elem104.read(iprot)
                        self.historys.append(_elem104)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.balance = Coin()
                    self.balance.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.hasNext = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinHistoryResult')
        if self.historys is not None:
            oprot.writeFieldBegin('historys', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.historys))
            for iter105 in self.historys:
                iter105.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.balance is not None:
            oprot.writeFieldBegin('balance', TType.STRUCT, 2)
            self.balance.write(oprot)
            oprot.writeFieldEnd()
        if self.hasNext is not None:
            oprot.writeFieldBegin('hasNext', TType.BOOL, 3)
            oprot.writeBool(self.hasNext)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinProductItem(object):
    """
    Attributes:
     - itemId
     - coin
     - freeCoin
     - currency
     - price
     - displayPrice
     - name
     - desc
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'itemId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'coin', None, None, ),  # 2
        (3, TType.I32, 'freeCoin', None, None, ),  # 3
        None,  # 4
        (5, TType.STRING, 'currency', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'price', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'displayPrice', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'name', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'desc', 'UTF8', None, ),  # 9
    )

    def __init__(self, itemId=None, coin=None, freeCoin=None, currency=None, price=None, displayPrice=None, name=None, desc=None,):
        self.itemId = itemId
        self.coin = coin
        self.freeCoin = freeCoin
        self.currency = currency
        self.price = price
        self.displayPrice = displayPrice
        self.name = name
        self.desc = desc

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.itemId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.coin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.freeCoin = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.displayPrice = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.desc = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinProductItem')
        if self.itemId is not None:
            oprot.writeFieldBegin('itemId', TType.STRING, 1)
            oprot.writeString(self.itemId.encode('utf-8') if sys.version_info[0] == 2 else self.itemId)
            oprot.writeFieldEnd()
        if self.coin is not None:
            oprot.writeFieldBegin('coin', TType.I32, 2)
            oprot.writeI32(self.coin)
            oprot.writeFieldEnd()
        if self.freeCoin is not None:
            oprot.writeFieldBegin('freeCoin', TType.I32, 3)
            oprot.writeI32(self.freeCoin)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 5)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 6)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.displayPrice is not None:
            oprot.writeFieldBegin('displayPrice', TType.STRING, 7)
            oprot.writeString(self.displayPrice.encode('utf-8') if sys.version_info[0] == 2 else self.displayPrice)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 8)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.desc is not None:
            oprot.writeFieldBegin('desc', TType.STRING, 9)
            oprot.writeString(self.desc.encode('utf-8') if sys.version_info[0] == 2 else self.desc)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinPurchaseConfirm(object):
    """
    Attributes:
     - orderId
     - appStoreCode
     - receipt
     - signature
     - seller
     - requestType
     - ignoreReceipt
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'orderId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'appStoreCode', None, None, ),  # 2
        (3, TType.STRING, 'receipt', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'signature', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'seller', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'requestType', 'UTF8', None, ),  # 6
        (7, TType.BOOL, 'ignoreReceipt', None, None, ),  # 7
    )

    def __init__(self, orderId=None, appStoreCode=None, receipt=None, signature=None, seller=None, requestType=None, ignoreReceipt=None,):
        self.orderId = orderId
        self.appStoreCode = appStoreCode
        self.receipt = receipt
        self.signature = signature
        self.seller = seller
        self.requestType = requestType
        self.ignoreReceipt = ignoreReceipt

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.orderId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.receipt = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.signature = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.seller = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.requestType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.ignoreReceipt = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinPurchaseConfirm')
        if self.orderId is not None:
            oprot.writeFieldBegin('orderId', TType.STRING, 1)
            oprot.writeString(self.orderId.encode('utf-8') if sys.version_info[0] == 2 else self.orderId)
            oprot.writeFieldEnd()
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 2)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.receipt is not None:
            oprot.writeFieldBegin('receipt', TType.STRING, 3)
            oprot.writeString(self.receipt.encode('utf-8') if sys.version_info[0] == 2 else self.receipt)
            oprot.writeFieldEnd()
        if self.signature is not None:
            oprot.writeFieldBegin('signature', TType.STRING, 4)
            oprot.writeString(self.signature.encode('utf-8') if sys.version_info[0] == 2 else self.signature)
            oprot.writeFieldEnd()
        if self.seller is not None:
            oprot.writeFieldBegin('seller', TType.STRING, 5)
            oprot.writeString(self.seller.encode('utf-8') if sys.version_info[0] == 2 else self.seller)
            oprot.writeFieldEnd()
        if self.requestType is not None:
            oprot.writeFieldBegin('requestType', TType.STRING, 6)
            oprot.writeString(self.requestType.encode('utf-8') if sys.version_info[0] == 2 else self.requestType)
            oprot.writeFieldEnd()
        if self.ignoreReceipt is not None:
            oprot.writeFieldBegin('ignoreReceipt', TType.BOOL, 7)
            oprot.writeBool(self.ignoreReceipt)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinPurchaseReservation(object):
    """
    Attributes:
     - productId
     - country
     - currency
     - price
     - appStoreCode
     - language
     - pgCode
     - redirectUrl
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'productId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'country', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'currency', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'price', 'UTF8', None, ),  # 4
        (5, TType.I32, 'appStoreCode', None, None, ),  # 5
        (6, TType.STRING, 'language', 'UTF8', None, ),  # 6
        (7, TType.I32, 'pgCode', None, None, ),  # 7
        (8, TType.STRING, 'redirectUrl', 'UTF8', None, ),  # 8
    )

    def __init__(self, productId=None, country=None, currency=None, price=None, appStoreCode=None, language=None, pgCode=None, redirectUrl=None,):
        self.productId = productId
        self.country = country
        self.currency = currency
        self.price = price
        self.appStoreCode = appStoreCode
        self.language = language
        self.pgCode = pgCode
        self.redirectUrl = redirectUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.pgCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.redirectUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinPurchaseReservation')
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 1)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 2)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 3)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 4)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 5)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 6)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.pgCode is not None:
            oprot.writeFieldBegin('pgCode', TType.I32, 7)
            oprot.writeI32(self.pgCode)
            oprot.writeFieldEnd()
        if self.redirectUrl is not None:
            oprot.writeFieldBegin('redirectUrl', TType.STRING, 8)
            oprot.writeString(self.redirectUrl.encode('utf-8') if sys.version_info[0] == 2 else self.redirectUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinUseReservationItem(object):
    """
    Attributes:
     - itemId
     - itemName
     - amount
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'itemId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'itemName', 'UTF8', None, ),  # 2
        (3, TType.I32, 'amount', None, None, ),  # 3
    )

    def __init__(self, itemId=None, itemName=None, amount=None,):
        self.itemId = itemId
        self.itemName = itemName
        self.amount = amount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.itemId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.itemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.amount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinUseReservationItem')
        if self.itemId is not None:
            oprot.writeFieldBegin('itemId', TType.STRING, 1)
            oprot.writeString(self.itemId.encode('utf-8') if sys.version_info[0] == 2 else self.itemId)
            oprot.writeFieldEnd()
        if self.itemName is not None:
            oprot.writeFieldBegin('itemName', TType.STRING, 2)
            oprot.writeString(self.itemName.encode('utf-8') if sys.version_info[0] == 2 else self.itemName)
            oprot.writeFieldEnd()
        if self.amount is not None:
            oprot.writeFieldBegin('amount', TType.I32, 3)
            oprot.writeI32(self.amount)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CoinUseReservation(object):
    """
    Attributes:
     - channelId
     - shopOrderId
     - appStoreCode
     - items
     - country
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'shopOrderId', 'UTF8', None, ),  # 2
        (3, TType.I32, 'appStoreCode', None, None, ),  # 3
        (4, TType.LIST, 'items', (TType.STRUCT, (CoinUseReservationItem, CoinUseReservationItem.thrift_spec), False), None, ),  # 4
        (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
    )

    def __init__(self, channelId=None, shopOrderId=None, appStoreCode=None, items=None, country=None,):
        self.channelId = channelId
        self.shopOrderId = shopOrderId
        self.appStoreCode = appStoreCode
        self.items = items
        self.country = country

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.shopOrderId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.items = []
                    (_etype109, _size106) = iprot.readListBegin()
                    for _i110 in range(_size106):
                        _elem111 = CoinUseReservationItem()
                        _elem111.read(iprot)
                        self.items.append(_elem111)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CoinUseReservation')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.shopOrderId is not None:
            oprot.writeFieldBegin('shopOrderId', TType.STRING, 2)
            oprot.writeString(self.shopOrderId.encode('utf-8') if sys.version_info[0] == 2 else self.shopOrderId)
            oprot.writeFieldEnd()
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 3)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.items is not None:
            oprot.writeFieldBegin('items', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.items))
            for iter112 in self.items:
                iter112.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CompactContact(object):
    """
    Attributes:
     - mid
     - createdTime
     - modifiedTime
     - status
     - settings
     - displayNameOverridden
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        (3, TType.I64, 'modifiedTime', None, None, ),  # 3
        (4, TType.I32, 'status', None, None, ),  # 4
        (5, TType.I64, 'settings', None, None, ),  # 5
        (6, TType.STRING, 'displayNameOverridden', 'UTF8', None, ),  # 6
    )

    def __init__(self, mid=None, createdTime=None, modifiedTime=None, status=None, settings=None, displayNameOverridden=None,):
        self.mid = mid
        self.createdTime = createdTime
        self.modifiedTime = modifiedTime
        self.status = status
        self.settings = settings
        self.displayNameOverridden = displayNameOverridden

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.modifiedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.settings = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.displayNameOverridden = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CompactContact')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.modifiedTime is not None:
            oprot.writeFieldBegin('modifiedTime', TType.I64, 3)
            oprot.writeI64(self.modifiedTime)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 4)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.settings is not None:
            oprot.writeFieldBegin('settings', TType.I64, 5)
            oprot.writeI64(self.settings)
            oprot.writeFieldEnd()
        if self.displayNameOverridden is not None:
            oprot.writeFieldBegin('displayNameOverridden', TType.STRING, 6)
            oprot.writeString(self.displayNameOverridden.encode('utf-8') if sys.version_info[0] == 2 else self.displayNameOverridden)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ContactModification(object):
    """
    Attributes:
     - type
     - luid
     - phones
     - emails
     - userids
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        (2, TType.STRING, 'luid', 'UTF8', None, ),  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.LIST, 'phones', (TType.STRING, 'UTF8', False), None, ),  # 11
        (12, TType.LIST, 'emails', (TType.STRING, 'UTF8', False), None, ),  # 12
        (13, TType.LIST, 'userids', (TType.STRING, 'UTF8', False), None, ),  # 13
    )

    def __init__(self, type=None, luid=None, phones=None, emails=None, userids=None,):
        self.type = type
        self.luid = luid
        self.phones = phones
        self.emails = emails
        self.userids = userids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.luid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.LIST:
                    self.phones = []
                    (_etype116, _size113) = iprot.readListBegin()
                    for _i117 in range(_size113):
                        _elem118 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.phones.append(_elem118)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.LIST:
                    self.emails = []
                    (_etype122, _size119) = iprot.readListBegin()
                    for _i123 in range(_size119):
                        _elem124 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.emails.append(_elem124)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.LIST:
                    self.userids = []
                    (_etype128, _size125) = iprot.readListBegin()
                    for _i129 in range(_size125):
                        _elem130 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userids.append(_elem130)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ContactModification')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.luid is not None:
            oprot.writeFieldBegin('luid', TType.STRING, 2)
            oprot.writeString(self.luid.encode('utf-8') if sys.version_info[0] == 2 else self.luid)
            oprot.writeFieldEnd()
        if self.phones is not None:
            oprot.writeFieldBegin('phones', TType.LIST, 11)
            oprot.writeListBegin(TType.STRING, len(self.phones))
            for iter131 in self.phones:
                oprot.writeString(iter131.encode('utf-8') if sys.version_info[0] == 2 else iter131)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.emails is not None:
            oprot.writeFieldBegin('emails', TType.LIST, 12)
            oprot.writeListBegin(TType.STRING, len(self.emails))
            for iter132 in self.emails:
                oprot.writeString(iter132.encode('utf-8') if sys.version_info[0] == 2 else iter132)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.userids is not None:
            oprot.writeFieldBegin('userids', TType.LIST, 13)
            oprot.writeListBegin(TType.STRING, len(self.userids))
            for iter133 in self.userids:
                oprot.writeString(iter133.encode('utf-8') if sys.version_info[0] == 2 else iter133)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ContactRegistration(object):
    """
    Attributes:
     - contact
     - luid
     - contactType
     - contactKey
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'contact', (Contact, Contact.thrift_spec), None, ),  # 1
        None,  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'luid', 'UTF8', None, ),  # 10
        (11, TType.I32, 'contactType', None, None, ),  # 11
        (12, TType.STRING, 'contactKey', 'UTF8', None, ),  # 12
    )

    def __init__(self, contact=None, luid=None, contactType=None, contactKey=None,):
        self.contact = contact
        self.luid = luid
        self.contactType = contactType
        self.contactKey = contactKey

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.contact = Contact()
                    self.contact.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.luid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.contactType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.contactKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ContactRegistration')
        if self.contact is not None:
            oprot.writeFieldBegin('contact', TType.STRUCT, 1)
            self.contact.write(oprot)
            oprot.writeFieldEnd()
        if self.luid is not None:
            oprot.writeFieldBegin('luid', TType.STRING, 10)
            oprot.writeString(self.luid.encode('utf-8') if sys.version_info[0] == 2 else self.luid)
            oprot.writeFieldEnd()
        if self.contactType is not None:
            oprot.writeFieldBegin('contactType', TType.I32, 11)
            oprot.writeI32(self.contactType)
            oprot.writeFieldEnd()
        if self.contactKey is not None:
            oprot.writeFieldBegin('contactKey', TType.STRING, 12)
            oprot.writeString(self.contactKey.encode('utf-8') if sys.version_info[0] == 2 else self.contactKey)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ContactReport(object):
    """
    Attributes:
     - mid
     - exists
     - contact
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.BOOL, 'exists', None, None, ),  # 2
        (3, TType.STRUCT, 'contact', (Contact, Contact.thrift_spec), None, ),  # 3
    )

    def __init__(self, mid=None, exists=None, contact=None,):
        self.mid = mid
        self.exists = exists
        self.contact = contact

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.exists = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.contact = Contact()
                    self.contact.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ContactReport')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.exists is not None:
            oprot.writeFieldBegin('exists', TType.BOOL, 2)
            oprot.writeBool(self.exists)
            oprot.writeFieldEnd()
        if self.contact is not None:
            oprot.writeFieldBegin('contact', TType.STRUCT, 3)
            self.contact.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ContactReportResult(object):
    """
    Attributes:
     - mid
     - exists
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.BOOL, 'exists', None, None, ),  # 2
    )

    def __init__(self, mid=None, exists=None,):
        self.mid = mid
        self.exists = exists

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.exists = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ContactReportResult')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.exists is not None:
            oprot.writeFieldBegin('exists', TType.BOOL, 2)
            oprot.writeBool(self.exists)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DeviceInfo(object):
    """
    Attributes:
     - deviceName
     - systemName
     - systemVersion
     - model
     - carrierCode
     - carrierName
     - applicationType
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'deviceName', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'systemName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'systemVersion', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'model', 'UTF8', None, ),  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.I32, 'carrierCode', None, None, ),  # 10
        (11, TType.STRING, 'carrierName', 'UTF8', None, ),  # 11
        None,  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        (20, TType.I32, 'applicationType', None, None, ),  # 20
    )

    def __init__(self, deviceName=None, systemName=None, systemVersion=None, model=None, carrierCode=None, carrierName=None, applicationType=None,):
        self.deviceName = deviceName
        self.systemName = systemName
        self.systemVersion = systemVersion
        self.model = model
        self.carrierCode = carrierCode
        self.carrierName = carrierName
        self.applicationType = applicationType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.deviceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.systemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.systemVersion = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.model = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.carrierCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.carrierName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I32:
                    self.applicationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('DeviceInfo')
        if self.deviceName is not None:
            oprot.writeFieldBegin('deviceName', TType.STRING, 1)
            oprot.writeString(self.deviceName.encode('utf-8') if sys.version_info[0] == 2 else self.deviceName)
            oprot.writeFieldEnd()
        if self.systemName is not None:
            oprot.writeFieldBegin('systemName', TType.STRING, 2)
            oprot.writeString(self.systemName.encode('utf-8') if sys.version_info[0] == 2 else self.systemName)
            oprot.writeFieldEnd()
        if self.systemVersion is not None:
            oprot.writeFieldBegin('systemVersion', TType.STRING, 3)
            oprot.writeString(self.systemVersion.encode('utf-8') if sys.version_info[0] == 2 else self.systemVersion)
            oprot.writeFieldEnd()
        if self.model is not None:
            oprot.writeFieldBegin('model', TType.STRING, 4)
            oprot.writeString(self.model.encode('utf-8') if sys.version_info[0] == 2 else self.model)
            oprot.writeFieldEnd()
        if self.carrierCode is not None:
            oprot.writeFieldBegin('carrierCode', TType.I32, 10)
            oprot.writeI32(self.carrierCode)
            oprot.writeFieldEnd()
        if self.carrierName is not None:
            oprot.writeFieldBegin('carrierName', TType.STRING, 11)
            oprot.writeString(self.carrierName.encode('utf-8') if sys.version_info[0] == 2 else self.carrierName)
            oprot.writeFieldEnd()
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.I32, 20)
            oprot.writeI32(self.applicationType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EmailConfirmation(object):
    """
    Attributes:
     - usePasswordSet
     - email
     - password
     - ignoreDuplication
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'usePasswordSet', None, None, ),  # 1
        (2, TType.STRING, 'email', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'password', 'UTF8', None, ),  # 3
        (4, TType.BOOL, 'ignoreDuplication', None, None, ),  # 4
    )

    def __init__(self, usePasswordSet=None, email=None, password=None, ignoreDuplication=None,):
        self.usePasswordSet = usePasswordSet
        self.email = email
        self.password = password
        self.ignoreDuplication = ignoreDuplication

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.usePasswordSet = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.ignoreDuplication = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('EmailConfirmation')
        if self.usePasswordSet is not None:
            oprot.writeFieldBegin('usePasswordSet', TType.BOOL, 1)
            oprot.writeBool(self.usePasswordSet)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 2)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 3)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.ignoreDuplication is not None:
            oprot.writeFieldBegin('ignoreDuplication', TType.BOOL, 4)
            oprot.writeBool(self.ignoreDuplication)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EmailConfirmationSession(object):
    """
    Attributes:
     - emailConfirmationType
     - verifier
     - targetEmail
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'emailConfirmationType', None, None, ),  # 1
        (2, TType.STRING, 'verifier', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'targetEmail', 'UTF8', None, ),  # 3
    )

    def __init__(self, emailConfirmationType=None, verifier=None, targetEmail=None,):
        self.emailConfirmationType = emailConfirmationType
        self.verifier = verifier
        self.targetEmail = targetEmail

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.emailConfirmationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.targetEmail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('EmailConfirmationSession')
        if self.emailConfirmationType is not None:
            oprot.writeFieldBegin('emailConfirmationType', TType.I32, 1)
            oprot.writeI32(self.emailConfirmationType)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 2)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.targetEmail is not None:
            oprot.writeFieldBegin('targetEmail', TType.STRING, 3)
            oprot.writeString(self.targetEmail.encode('utf-8') if sys.version_info[0] == 2 else self.targetEmail)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FriendChannelMatrix(object):
    """
    Attributes:
     - channelId
     - representMid
     - count
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'representMid', 'UTF8', None, ),  # 2
        (3, TType.I32, 'count', None, None, ),  # 3
    )

    def __init__(self, channelId=None, representMid=None, count=None,):
        self.channelId = channelId
        self.representMid = representMid
        self.count = count

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.representMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('FriendChannelMatrix')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.representMid is not None:
            oprot.writeFieldBegin('representMid', TType.STRING, 2)
            oprot.writeString(self.representMid.encode('utf-8') if sys.version_info[0] == 2 else self.representMid)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 3)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FriendChannelMatricesResponse(object):
    """
    Attributes:
     - expires
     - matrices
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'expires', None, None, ),  # 1
        (2, TType.LIST, 'matrices', (TType.STRUCT, (FriendChannelMatrix, FriendChannelMatrix.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, expires=None, matrices=None,):
        self.expires = expires
        self.matrices = matrices

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.expires = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.matrices = []
                    (_etype137, _size134) = iprot.readListBegin()
                    for _i138 in range(_size134):
                        _elem139 = FriendChannelMatrix()
                        _elem139.read(iprot)
                        self.matrices.append(_elem139)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('FriendChannelMatricesResponse')
        if self.expires is not None:
            oprot.writeFieldBegin('expires', TType.I64, 1)
            oprot.writeI64(self.expires)
            oprot.writeFieldEnd()
        if self.matrices is not None:
            oprot.writeFieldBegin('matrices', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.matrices))
            for iter140 in self.matrices:
                iter140.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Geolocation(object):
    """
    Attributes:
     - longitude
     - latitude
    """

    thrift_spec = (
        None,  # 0
        (1, TType.DOUBLE, 'longitude', None, None, ),  # 1
        (2, TType.DOUBLE, 'latitude', None, None, ),  # 2
    )

    def __init__(self, longitude=None, latitude=None,):
        self.longitude = longitude
        self.latitude = latitude

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.longitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.latitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Geolocation')
        if self.longitude is not None:
            oprot.writeFieldBegin('longitude', TType.DOUBLE, 1)
            oprot.writeDouble(self.longitude)
            oprot.writeFieldEnd()
        if self.latitude is not None:
            oprot.writeFieldBegin('latitude', TType.DOUBLE, 2)
            oprot.writeDouble(self.latitude)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class NotificationTarget(object):
    """
    Attributes:
     - applicationType
     - applicationVersion
     - region
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'applicationType', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'applicationVersion', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'region', 'UTF8', None, ),  # 3
    )

    def __init__(self, applicationType=None, applicationVersion=None, region=None,):
        self.applicationType = applicationType
        self.applicationVersion = applicationVersion
        self.region = region

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.applicationType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.applicationVersion = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.region = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('NotificationTarget')
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.STRING, 1)
            oprot.writeString(self.applicationType.encode('utf-8') if sys.version_info[0] == 2 else self.applicationType)
            oprot.writeFieldEnd()
        if self.applicationVersion is not None:
            oprot.writeFieldBegin('applicationVersion', TType.STRING, 2)
            oprot.writeString(self.applicationVersion.encode('utf-8') if sys.version_info[0] == 2 else self.applicationVersion)
            oprot.writeFieldEnd()
        if self.region is not None:
            oprot.writeFieldBegin('region', TType.STRING, 3)
            oprot.writeString(self.region.encode('utf-8') if sys.version_info[0] == 2 else self.region)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GlobalEvent(object):
    """
    Attributes:
     - key
     - targets
     - createdTime
     - data
     - maxDelay
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'key', 'UTF8', None, ),  # 1
        (2, TType.LIST, 'targets', (TType.STRUCT, (NotificationTarget, NotificationTarget.thrift_spec), False), None, ),  # 2
        (3, TType.I64, 'createdTime', None, None, ),  # 3
        (4, TType.I64, 'data', None, None, ),  # 4
        (5, TType.I32, 'maxDelay', None, None, ),  # 5
    )

    def __init__(self, key=None, targets=None, createdTime=None, data=None, maxDelay=None,):
        self.key = key
        self.targets = targets
        self.createdTime = createdTime
        self.data = data
        self.maxDelay = maxDelay

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.targets = []
                    (_etype144, _size141) = iprot.readListBegin()
                    for _i145 in range(_size141):
                        _elem146 = NotificationTarget()
                        _elem146.read(iprot)
                        self.targets.append(_elem146)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.data = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.maxDelay = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('GlobalEvent')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeString(self.key.encode('utf-8') if sys.version_info[0] == 2 else self.key)
            oprot.writeFieldEnd()
        if self.targets is not None:
            oprot.writeFieldBegin('targets', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.targets))
            for iter147 in self.targets:
                iter147.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 3)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.I64, 4)
            oprot.writeI64(self.data)
            oprot.writeFieldEnd()
        if self.maxDelay is not None:
            oprot.writeFieldBegin('maxDelay', TType.I32, 5)
            oprot.writeI32(self.maxDelay)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Group(object):
    """
    Attributes:
     - id
     - createdTime
     - name
     - pictureStatus
     - members
     - creator
     - invitee
     - notificationDisabled
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'name', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 11
        None,  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        (20, TType.LIST, 'members', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 20
        (21, TType.STRUCT, 'creator', (Contact, Contact.thrift_spec), None, ),  # 21
        (22, TType.LIST, 'invitee', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 22
        None,  # 23
        None,  # 24
        None,  # 25
        None,  # 26
        None,  # 27
        None,  # 28
        None,  # 29
        None,  # 30
        (31, TType.BOOL, 'notificationDisabled', None, None, ),  # 31
    )

    def __init__(self, id=None, createdTime=None, name=None, pictureStatus=None, members=None, creator=None, invitee=None, notificationDisabled=None,):
        self.id = id
        self.createdTime = createdTime
        self.name = name
        self.pictureStatus = pictureStatus
        self.members = members
        self.creator = creator
        self.invitee = invitee
        self.notificationDisabled = notificationDisabled

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.LIST:
                    self.members = []
                    (_etype151, _size148) = iprot.readListBegin()
                    for _i152 in range(_size148):
                        _elem153 = Contact()
                        _elem153.read(iprot)
                        self.members.append(_elem153)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRUCT:
                    self.creator = Contact()
                    self.creator.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.LIST:
                    self.invitee = []
                    (_etype157, _size154) = iprot.readListBegin()
                    for _i158 in range(_size154):
                        _elem159 = Contact()
                        _elem159.read(iprot)
                        self.invitee.append(_elem159)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.notificationDisabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Group')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 10)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 11)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.members is not None:
            oprot.writeFieldBegin('members', TType.LIST, 20)
            oprot.writeListBegin(TType.STRUCT, len(self.members))
            for iter160 in self.members:
                iter160.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.creator is not None:
            oprot.writeFieldBegin('creator', TType.STRUCT, 21)
            self.creator.write(oprot)
            oprot.writeFieldEnd()
        if self.invitee is not None:
            oprot.writeFieldBegin('invitee', TType.LIST, 22)
            oprot.writeListBegin(TType.STRUCT, len(self.invitee))
            for iter161 in self.invitee:
                iter161.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.notificationDisabled is not None:
            oprot.writeFieldBegin('notificationDisabled', TType.BOOL, 31)
            oprot.writeBool(self.notificationDisabled)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class IdentityCredential(object):
    """
    Attributes:
     - provider
     - identifier
     - password
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'provider', None, None, ),  # 1
        (2, TType.STRING, 'identifier', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'password', 'UTF8', None, ),  # 3
    )

    def __init__(self, provider=None, identifier=None, password=None,):
        self.provider = provider
        self.identifier = identifier
        self.password = password

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.provider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.identifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('IdentityCredential')
        if self.provider is not None:
            oprot.writeFieldBegin('provider', TType.I32, 1)
            oprot.writeI32(self.provider)
            oprot.writeFieldEnd()
        if self.identifier is not None:
            oprot.writeFieldBegin('identifier', TType.STRING, 2)
            oprot.writeString(self.identifier.encode('utf-8') if sys.version_info[0] == 2 else self.identifier)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 3)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LastReadMessageId(object):
    """
    Attributes:
     - mid
     - lastReadMessageId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'lastReadMessageId', 'UTF8', None, ),  # 2
    )

    def __init__(self, mid=None, lastReadMessageId=None,):
        self.mid = mid
        self.lastReadMessageId = lastReadMessageId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.lastReadMessageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LastReadMessageId')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.lastReadMessageId is not None:
            oprot.writeFieldBegin('lastReadMessageId', TType.STRING, 2)
            oprot.writeString(self.lastReadMessageId.encode('utf-8') if sys.version_info[0] == 2 else self.lastReadMessageId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LastReadMessageIds(object):
    """
    Attributes:
     - chatId
     - lastReadMessageIds
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'chatId', 'UTF8', None, ),  # 1
        (2, TType.LIST, 'lastReadMessageIds', (TType.STRUCT, (LastReadMessageId, LastReadMessageId.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, chatId=None, lastReadMessageIds=None,):
        self.chatId = chatId
        self.lastReadMessageIds = lastReadMessageIds

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.chatId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.lastReadMessageIds = []
                    (_etype165, _size162) = iprot.readListBegin()
                    for _i166 in range(_size162):
                        _elem167 = LastReadMessageId()
                        _elem167.read(iprot)
                        self.lastReadMessageIds.append(_elem167)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LastReadMessageIds')
        if self.chatId is not None:
            oprot.writeFieldBegin('chatId', TType.STRING, 1)
            oprot.writeString(self.chatId.encode('utf-8') if sys.version_info[0] == 2 else self.chatId)
            oprot.writeFieldEnd()
        if self.lastReadMessageIds is not None:
            oprot.writeFieldBegin('lastReadMessageIds', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.lastReadMessageIds))
            for iter168 in self.lastReadMessageIds:
                iter168.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class VerificationSessionData(object):
    """
    Attributes:
     - sessionId
     - method
     - callback
     - nomarizediPhone
     - countryCode
     - nationalSignificantNumber
     - availableVerificationMethods
     - callerIdMask
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'sessionId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'method', None, None, ),  # 2
        (3, TType.STRING, 'callback', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'nomarizediPhone', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'countryCode', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'nationalSignificantNumber', 'UTF8', None, ),  # 6
        (7, TType.I32, 'availableVerificationMethods', None, None, ),  # 7
        (8, TType.STRING, 'callerIdMask', 'UTF8', None, ),  # 8
    )

    def __init__(self, sessionId=None, method=None, callback=None, nomarizediPhone=None, countryCode=None, nationalSignificantNumber=None, availableVerificationMethods=None, callerIdMask=None,):
        self.sessionId = sessionId
        self.method = method
        self.callback = callback
        self.nomarizediPhone = nomarizediPhone
        self.countryCode = countryCode
        self.nationalSignificantNumber = nationalSignificantNumber
        self.availableVerificationMethods = availableVerificationMethods
        self.callerIdMask = callerIdMask

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.sessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.method = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.callback = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.nomarizediPhone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.countryCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.nationalSignificantNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.availableVerificationMethods = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.callerIdMask = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('VerificationSessionData')
        if self.sessionId is not None:
            oprot.writeFieldBegin('sessionId', TType.STRING, 1)
            oprot.writeString(self.sessionId.encode('utf-8') if sys.version_info[0] == 2 else self.sessionId)
            oprot.writeFieldEnd()
        if self.method is not None:
            oprot.writeFieldBegin('method', TType.I32, 2)
            oprot.writeI32(self.method)
            oprot.writeFieldEnd()
        if self.callback is not None:
            oprot.writeFieldBegin('callback', TType.STRING, 3)
            oprot.writeString(self.callback.encode('utf-8') if sys.version_info[0] == 2 else self.callback)
            oprot.writeFieldEnd()
        if self.nomarizediPhone is not None:
            oprot.writeFieldBegin('nomarizediPhone', TType.STRING, 4)
            oprot.writeString(self.nomarizediPhone.encode('utf-8') if sys.version_info[0] == 2 else self.nomarizediPhone)
            oprot.writeFieldEnd()
        if self.countryCode is not None:
            oprot.writeFieldBegin('countryCode', TType.STRING, 5)
            oprot.writeString(self.countryCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryCode)
            oprot.writeFieldEnd()
        if self.nationalSignificantNumber is not None:
            oprot.writeFieldBegin('nationalSignificantNumber', TType.STRING, 6)
            oprot.writeString(self.nationalSignificantNumber.encode('utf-8') if sys.version_info[0] == 2 else self.nationalSignificantNumber)
            oprot.writeFieldEnd()
        if self.availableVerificationMethods is not None:
            oprot.writeFieldBegin('availableVerificationMethods', TType.I32, 7)
            oprot.writeI32(self.availableVerificationMethods)
            oprot.writeFieldEnd()
        if self.callerIdMask is not None:
            oprot.writeFieldBegin('callerIdMask', TType.STRING, 8)
            oprot.writeString(self.callerIdMask.encode('utf-8') if sys.version_info[0] == 2 else self.callerIdMask)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginResult(object):
    """
    Attributes:
     - authToken
     - certificate
     - verifier
     - pinCode
     - type
     - lastPrimaryBindTime
     - displayMessage
     - sessionForSMSConfirm
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'authToken', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'certificate', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'verifier', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'pinCode', 'UTF8', None, ),  # 4
        (5, TType.I32, 'type', None, None, ),  # 5
        (6, TType.I64, 'lastPrimaryBindTime', None, None, ),  # 6
        (7, TType.STRING, 'displayMessage', 'UTF8', None, ),  # 7
        (8, TType.STRUCT, 'sessionForSMSConfirm', (VerificationSessionData, VerificationSessionData.thrift_spec), None, ),  # 8
    )

    def __init__(self, authToken=None, certificate=None, verifier=None, pinCode=None, type=None, lastPrimaryBindTime=None, displayMessage=None, sessionForSMSConfirm=None,):
        self.authToken = authToken
        self.certificate = certificate
        self.verifier = verifier
        self.pinCode = pinCode
        self.type = type
        self.lastPrimaryBindTime = lastPrimaryBindTime
        self.displayMessage = displayMessage
        self.sessionForSMSConfirm = sessionForSMSConfirm

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.authToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pinCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.lastPrimaryBindTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.displayMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.sessionForSMSConfirm = VerificationSessionData()
                    self.sessionForSMSConfirm.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LoginResult')
        if self.authToken is not None:
            oprot.writeFieldBegin('authToken', TType.STRING, 1)
            oprot.writeString(self.authToken.encode('utf-8') if sys.version_info[0] == 2 else self.authToken)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 2)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 3)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.pinCode is not None:
            oprot.writeFieldBegin('pinCode', TType.STRING, 4)
            oprot.writeString(self.pinCode.encode('utf-8') if sys.version_info[0] == 2 else self.pinCode)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.lastPrimaryBindTime is not None:
            oprot.writeFieldBegin('lastPrimaryBindTime', TType.I64, 6)
            oprot.writeI64(self.lastPrimaryBindTime)
            oprot.writeFieldEnd()
        if self.displayMessage is not None:
            oprot.writeFieldBegin('displayMessage', TType.STRING, 7)
            oprot.writeString(self.displayMessage.encode('utf-8') if sys.version_info[0] == 2 else self.displayMessage)
            oprot.writeFieldEnd()
        if self.sessionForSMSConfirm is not None:
            oprot.writeFieldBegin('sessionForSMSConfirm', TType.STRUCT, 8)
            self.sessionForSMSConfirm.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginResult2(object):
    """
    Attributes:
     - key
     - fid_4
     - fid_5
     - fid_6
    """

    thrift_spec = (
        None,  # 0
        None,  # 1
        None,  # 2
        (3, TType.STRING, 'key', 'BINARY', None, ),  # 3
        (4, TType.STRING, 'fid_4', 'BINARY', None, ),  # 4
        (5, TType.I32, 'fid_5', None, None, ),  # 5
        (6, TType.I64, 'fid_6', None, None, ),  # 6
    )

    def __init__(self, key=None, fid_4=None, fid_5=None, fid_6=None,):
        self.key = key
        self.fid_4 = fid_4
        self.fid_5 = fid_5
        self.fid_6 = fid_6

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 3:
                if ftype == TType.STRING:
                    self.key = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.fid_4 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fid_5 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.fid_6 = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LoginResult2')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 3)
            oprot.writeBinary(self.key)
            oprot.writeFieldEnd()
        if self.fid_4 is not None:
            oprot.writeFieldBegin('fid_4', TType.STRING, 4)
            oprot.writeBinary(self.fid_4)
            oprot.writeFieldEnd()
        if self.fid_5 is not None:
            oprot.writeFieldBegin('fid_5', TType.I32, 5)
            oprot.writeI32(self.fid_5)
            oprot.writeFieldEnd()
        if self.fid_6 is not None:
            oprot.writeFieldBegin('fid_6', TType.I64, 6)
            oprot.writeI64(self.fid_6)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class loginRequest(object):
    """
    Attributes:
     - type
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
     - verifier
     - secret
     - e2eeVersion
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        (2, TType.I32, 'identityProvider', None, None, ),  # 2
        (3, TType.STRING, 'identifier', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'password', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'keepLoggedIn', None, None, ),  # 5
        (6, TType.STRING, 'accessLocation', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'systemName', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'certificate', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'verifier', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'secret', 'UTF8', None, ),  # 10
        (11, TType.I32, 'e2eeVersion', None, None, ),  # 11
    )

    def __init__(self, type=None, identityProvider=None, identifier=None, password=None, keepLoggedIn=None, accessLocation=None, systemName=None, certificate=None, verifier=None, secret=None, e2eeVersion=None,):
        self.type = type
        self.identityProvider = identityProvider
        self.identifier = identifier
        self.password = password
        self.keepLoggedIn = keepLoggedIn
        self.accessLocation = accessLocation
        self.systemName = systemName
        self.certificate = certificate
        self.verifier = verifier
        self.secret = secret
        self.e2eeVersion = e2eeVersion

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.identityProvider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.identifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.keepLoggedIn = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.accessLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.systemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.secret = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.e2eeVersion = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('loginRequest')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.identityProvider is not None:
            oprot.writeFieldBegin('identityProvider', TType.I32, 2)
            oprot.writeI32(self.identityProvider)
            oprot.writeFieldEnd()
        if self.identifier is not None:
            oprot.writeFieldBegin('identifier', TType.STRING, 3)
            oprot.writeString(self.identifier.encode('utf-8') if sys.version_info[0] == 2 else self.identifier)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 4)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.keepLoggedIn is not None:
            oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 5)
            oprot.writeBool(self.keepLoggedIn)
            oprot.writeFieldEnd()
        if self.accessLocation is not None:
            oprot.writeFieldBegin('accessLocation', TType.STRING, 6)
            oprot.writeString(self.accessLocation.encode('utf-8') if sys.version_info[0] == 2 else self.accessLocation)
            oprot.writeFieldEnd()
        if self.systemName is not None:
            oprot.writeFieldBegin('systemName', TType.STRING, 7)
            oprot.writeString(self.systemName.encode('utf-8') if sys.version_info[0] == 2 else self.systemName)
            oprot.writeFieldEnd()
        if self.certificate is not None:
            oprot.writeFieldBegin('certificate', TType.STRING, 8)
            oprot.writeString(self.certificate.encode('utf-8') if sys.version_info[0] == 2 else self.certificate)
            oprot.writeFieldEnd()
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 9)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.secret is not None:
            oprot.writeFieldBegin('secret', TType.STRING, 10)
            oprot.writeString(self.secret.encode('utf-8') if sys.version_info[0] == 2 else self.secret)
            oprot.writeFieldEnd()
        if self.e2eeVersion is not None:
            oprot.writeFieldBegin('e2eeVersion', TType.I32, 11)
            oprot.writeI32(self.e2eeVersion)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class loginRequest2(object):
    """
    Attributes:
     - fid_3
     - fid_4
     - fid_5
     - fid_6
     - fid_9
     - fid_10
     - fid_11
     - fid_12
     - fid_13
    """

    thrift_spec = (
        None,  # 0
        None,  # 1
        None,  # 2
        (3, TType.I32, 'fid_3', None, None, ),  # 3
        (4, TType.I32, 'fid_4', None, None, ),  # 4
        (5, TType.STRING, 'fid_5', 'BINARY', None, ),  # 5
        (6, TType.STRING, 'fid_6', 'BINARY', None, ),  # 6
        None,  # 7
        None,  # 8
        (9, TType.STRING, 'fid_9', 'BINARY', None, ),  # 9
        (10, TType.STRING, 'fid_10', 'BINARY', None, ),  # 10
        (11, TType.STRING, 'fid_11', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'fid_12', 'UTF8', None, ),  # 12
        (13, TType.I32, 'fid_13', None, None, ),  # 13
    )

    def __init__(self, fid_3=None, fid_4=None, fid_5=None, fid_6=None, fid_9=None, fid_10=None, fid_11=None, fid_12=None, fid_13=None,):
        self.fid_3 = fid_3
        self.fid_4 = fid_4
        self.fid_5 = fid_5
        self.fid_6 = fid_6
        self.fid_9 = fid_9
        self.fid_10 = fid_10
        self.fid_11 = fid_11
        self.fid_12 = fid_12
        self.fid_13 = fid_13

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 3:
                if ftype == TType.I32:
                    self.fid_3 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.fid_4 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.fid_5 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.fid_6 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.fid_9 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.fid_10 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.fid_11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.fid_12 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.fid_13 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('loginRequest2')
        if self.fid_3 is not None:
            oprot.writeFieldBegin('fid_3', TType.I32, 3)
            oprot.writeI32(self.fid_3)
            oprot.writeFieldEnd()
        if self.fid_4 is not None:
            oprot.writeFieldBegin('fid_4', TType.I32, 4)
            oprot.writeI32(self.fid_4)
            oprot.writeFieldEnd()
        if self.fid_5 is not None:
            oprot.writeFieldBegin('fid_5', TType.STRING, 5)
            oprot.writeBinary(self.fid_5)
            oprot.writeFieldEnd()
        if self.fid_6 is not None:
            oprot.writeFieldBegin('fid_6', TType.STRING, 6)
            oprot.writeBinary(self.fid_6)
            oprot.writeFieldEnd()
        if self.fid_9 is not None:
            oprot.writeFieldBegin('fid_9', TType.STRING, 9)
            oprot.writeBinary(self.fid_9)
            oprot.writeFieldEnd()
        if self.fid_10 is not None:
            oprot.writeFieldBegin('fid_10', TType.STRING, 10)
            oprot.writeBinary(self.fid_10)
            oprot.writeFieldEnd()
        if self.fid_11 is not None:
            oprot.writeFieldBegin('fid_11', TType.STRING, 11)
            oprot.writeString(self.fid_11.encode('utf-8') if sys.version_info[0] == 2 else self.fid_11)
            oprot.writeFieldEnd()
        if self.fid_12 is not None:
            oprot.writeFieldBegin('fid_12', TType.STRING, 12)
            oprot.writeString(self.fid_12.encode('utf-8') if sys.version_info[0] == 2 else self.fid_12)
            oprot.writeFieldEnd()
        if self.fid_13 is not None:
            oprot.writeFieldBegin('fid_13', TType.I32, 13)
            oprot.writeI32(self.fid_13)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginSession(object):
    """
    Attributes:
     - tokenKey
     - expirationTime
     - applicationType
     - systemName
     - accessLocation
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'tokenKey', 'UTF8', None, ),  # 1
        None,  # 2
        (3, TType.I64, 'expirationTime', None, None, ),  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.I32, 'applicationType', None, None, ),  # 11
        (12, TType.STRING, 'systemName', 'UTF8', None, ),  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        None,  # 21
        (22, TType.STRING, 'accessLocation', 'UTF8', None, ),  # 22
    )

    def __init__(self, tokenKey=None, expirationTime=None, applicationType=None, systemName=None, accessLocation=None,):
        self.tokenKey = tokenKey
        self.expirationTime = expirationTime
        self.applicationType = applicationType
        self.systemName = systemName
        self.accessLocation = accessLocation

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.tokenKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.expirationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.applicationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.systemName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.accessLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LoginSession')
        if self.tokenKey is not None:
            oprot.writeFieldBegin('tokenKey', TType.STRING, 1)
            oprot.writeString(self.tokenKey.encode('utf-8') if sys.version_info[0] == 2 else self.tokenKey)
            oprot.writeFieldEnd()
        if self.expirationTime is not None:
            oprot.writeFieldBegin('expirationTime', TType.I64, 3)
            oprot.writeI64(self.expirationTime)
            oprot.writeFieldEnd()
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.I32, 11)
            oprot.writeI32(self.applicationType)
            oprot.writeFieldEnd()
        if self.systemName is not None:
            oprot.writeFieldBegin('systemName', TType.STRING, 12)
            oprot.writeString(self.systemName.encode('utf-8') if sys.version_info[0] == 2 else self.systemName)
            oprot.writeFieldEnd()
        if self.accessLocation is not None:
            oprot.writeFieldBegin('accessLocation', TType.STRING, 22)
            oprot.writeString(self.accessLocation.encode('utf-8') if sys.version_info[0] == 2 else self.accessLocation)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Message(object):
    """
    Attributes:
     - from_
     - to
     - toType
     - id
     - createdTime
     - deliveredTime
     - text
     - location
     - hasContent
     - contentType
     - contentPreview
     - contentMetadata
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'from_', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'to', 'UTF8', None, ),  # 2
        (3, TType.I32, 'toType', None, None, ),  # 3
        (4, TType.STRING, 'id', 'UTF8', None, ),  # 4
        (5, TType.I64, 'createdTime', None, None, ),  # 5
        (6, TType.I64, 'deliveredTime', None, None, ),  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'text', 'UTF8', None, ),  # 10
        (11, TType.STRUCT, 'location', (Location, Location.thrift_spec), None, ),  # 11
        None,  # 12
        None,  # 13
        (14, TType.BOOL, 'hasContent', None, None, ),  # 14
        (15, TType.I32, 'contentType', None, None, ),  # 15
        None,  # 16
        (17, TType.STRING, 'contentPreview', 'BINARY', None, ),  # 17
        (18, TType.MAP, 'contentMetadata', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 18
    )

    def __init__(self, from_=None, to=None, toType=None, id=None, createdTime=None, deliveredTime=None, text=None, location=None, hasContent=None, contentType=None, contentPreview=None, contentMetadata=None,):
        self.from_ = from_
        self.to = to
        self.toType = toType
        self.id = id
        self.createdTime = createdTime
        self.deliveredTime = deliveredTime
        self.text = text
        self.location = location
        self.hasContent = hasContent
        self.contentType = contentType
        self.contentPreview = contentPreview
        self.contentMetadata = contentMetadata

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.from_ = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.to = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.toType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.deliveredTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.location = Location()
                    self.location.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.BOOL:
                    self.hasContent = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.contentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.contentPreview = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.MAP:
                    self.contentMetadata = {}
                    (_ktype170, _vtype171, _size169) = iprot.readMapBegin()
                    for _i173 in range(_size169):
                        _key174 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val175 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.contentMetadata[_key174] = _val175
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Message')
        if self.from_ is not None:
            oprot.writeFieldBegin('from_', TType.STRING, 1)
            oprot.writeString(self.from_.encode('utf-8') if sys.version_info[0] == 2 else self.from_)
            oprot.writeFieldEnd()
        if self.to is not None:
            oprot.writeFieldBegin('to', TType.STRING, 2)
            oprot.writeString(self.to.encode('utf-8') if sys.version_info[0] == 2 else self.to)
            oprot.writeFieldEnd()
        if self.toType is not None:
            oprot.writeFieldBegin('toType', TType.I32, 3)
            oprot.writeI32(self.toType)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 4)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 5)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.deliveredTime is not None:
            oprot.writeFieldBegin('deliveredTime', TType.I64, 6)
            oprot.writeI64(self.deliveredTime)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 10)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.location is not None:
            oprot.writeFieldBegin('location', TType.STRUCT, 11)
            self.location.write(oprot)
            oprot.writeFieldEnd()
        if self.hasContent is not None:
            oprot.writeFieldBegin('hasContent', TType.BOOL, 14)
            oprot.writeBool(self.hasContent)
            oprot.writeFieldEnd()
        if self.contentType is not None:
            oprot.writeFieldBegin('contentType', TType.I32, 15)
            oprot.writeI32(self.contentType)
            oprot.writeFieldEnd()
        if self.contentPreview is not None:
            oprot.writeFieldBegin('contentPreview', TType.STRING, 17)
            oprot.writeBinary(self.contentPreview)
            oprot.writeFieldEnd()
        if self.contentMetadata is not None:
            oprot.writeFieldBegin('contentMetadata', TType.MAP, 18)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.contentMetadata))
            for kiter176, viter177 in self.contentMetadata.items():
                oprot.writeString(kiter176.encode('utf-8') if sys.version_info[0] == 2 else kiter176)
                oprot.writeString(viter177.encode('utf-8') if sys.version_info[0] == 2 else viter177)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MessageOperation(object):
    """
    Attributes:
     - revision
     - createdTime
     - type
     - reqSeq
     - status
     - param1
     - param2
     - param3
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'revision', None, None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        (3, TType.I32, 'type', None, None, ),  # 3
        (4, TType.I32, 'reqSeq', None, None, ),  # 4
        (5, TType.I32, 'status', None, None, ),  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'param1', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'param2', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'param3', 'UTF8', None, ),  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        (20, TType.STRUCT, 'message', (Message, Message.thrift_spec), None, ),  # 20
    )

    def __init__(self, revision=None, createdTime=None, type=None, reqSeq=None, status=None, param1=None, param2=None, param3=None, message=None,):
        self.revision = revision
        self.createdTime = createdTime
        self.type = type
        self.reqSeq = reqSeq
        self.status = status
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.reqSeq = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.param1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.param2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.param3 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MessageOperation')
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 1)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.reqSeq is not None:
            oprot.writeFieldBegin('reqSeq', TType.I32, 4)
            oprot.writeI32(self.reqSeq)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 5)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.param1 is not None:
            oprot.writeFieldBegin('param1', TType.STRING, 10)
            oprot.writeString(self.param1.encode('utf-8') if sys.version_info[0] == 2 else self.param1)
            oprot.writeFieldEnd()
        if self.param2 is not None:
            oprot.writeFieldBegin('param2', TType.STRING, 11)
            oprot.writeString(self.param2.encode('utf-8') if sys.version_info[0] == 2 else self.param2)
            oprot.writeFieldEnd()
        if self.param3 is not None:
            oprot.writeFieldBegin('param3', TType.STRING, 12)
            oprot.writeString(self.param3.encode('utf-8') if sys.version_info[0] == 2 else self.param3)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 20)
            self.message.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MessageOperations(object):
    """
    Attributes:
     - operations
     - endFlag
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'operations', (TType.STRUCT, (MessageOperation, MessageOperation.thrift_spec), False), None, ),  # 1
        (2, TType.BOOL, 'endFlag', None, None, ),  # 2
    )

    def __init__(self, operations=None, endFlag=None,):
        self.operations = operations
        self.endFlag = endFlag

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.operations = []
                    (_etype181, _size178) = iprot.readListBegin()
                    for _i182 in range(_size178):
                        _elem183 = MessageOperation()
                        _elem183.read(iprot)
                        self.operations.append(_elem183)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.endFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MessageOperations')
        if self.operations is not None:
            oprot.writeFieldBegin('operations', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.operations))
            for iter184 in self.operations:
                iter184.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.endFlag is not None:
            oprot.writeFieldBegin('endFlag', TType.BOOL, 2)
            oprot.writeBool(self.endFlag)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MetaProfile(object):
    """
    Attributes:
     - createTime
     - regionCode
     - identities
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'createTime', None, None, ),  # 1
        (2, TType.STRING, 'regionCode', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'identities', (TType.I32, None, TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, createTime=None, regionCode=None, identities=None,):
        self.createTime = createTime
        self.regionCode = regionCode
        self.identities = identities

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.createTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.regionCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.identities = {}
                    (_ktype186, _vtype187, _size185) = iprot.readMapBegin()
                    for _i189 in range(_size185):
                        _key190 = iprot.readI32()
                        _val191 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.identities[_key190] = _val191
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('MetaProfile')
        if self.createTime is not None:
            oprot.writeFieldBegin('createTime', TType.I64, 1)
            oprot.writeI64(self.createTime)
            oprot.writeFieldEnd()
        if self.regionCode is not None:
            oprot.writeFieldBegin('regionCode', TType.STRING, 2)
            oprot.writeString(self.regionCode.encode('utf-8') if sys.version_info[0] == 2 else self.regionCode)
            oprot.writeFieldEnd()
        if self.identities is not None:
            oprot.writeFieldBegin('identities', TType.MAP, 3)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.identities))
            for kiter192, viter193 in self.identities.items():
                oprot.writeI32(kiter192)
                oprot.writeString(viter193.encode('utf-8') if sys.version_info[0] == 2 else viter193)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class NotificationItem(object):
    """
    Attributes:
     - id
     - from_
     - to
     - fromChannel
     - toChannel
     - revision
     - createdTime
     - content
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'from_', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'to', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'fromChannel', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'toChannel', 'UTF8', None, ),  # 5
        None,  # 6
        (7, TType.I64, 'revision', None, None, ),  # 7
        (8, TType.I64, 'createdTime', None, None, ),  # 8
        (9, TType.MAP, 'content', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 9
    )

    def __init__(self, id=None, from_=None, to=None, fromChannel=None, toChannel=None, revision=None, createdTime=None, content=None,):
        self.id = id
        self.from_ = from_
        self.to = to
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.revision = revision
        self.createdTime = createdTime
        self.content = content

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.from_ = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.to = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.fromChannel = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.toChannel = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.MAP:
                    self.content = {}
                    (_ktype195, _vtype196, _size194) = iprot.readMapBegin()
                    for _i198 in range(_size194):
                        _key199 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val200 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.content[_key199] = _val200
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('NotificationItem')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.from_ is not None:
            oprot.writeFieldBegin('from_', TType.STRING, 2)
            oprot.writeString(self.from_.encode('utf-8') if sys.version_info[0] == 2 else self.from_)
            oprot.writeFieldEnd()
        if self.to is not None:
            oprot.writeFieldBegin('to', TType.STRING, 3)
            oprot.writeString(self.to.encode('utf-8') if sys.version_info[0] == 2 else self.to)
            oprot.writeFieldEnd()
        if self.fromChannel is not None:
            oprot.writeFieldBegin('fromChannel', TType.STRING, 4)
            oprot.writeString(self.fromChannel.encode('utf-8') if sys.version_info[0] == 2 else self.fromChannel)
            oprot.writeFieldEnd()
        if self.toChannel is not None:
            oprot.writeFieldBegin('toChannel', TType.STRING, 5)
            oprot.writeString(self.toChannel.encode('utf-8') if sys.version_info[0] == 2 else self.toChannel)
            oprot.writeFieldEnd()
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 7)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 8)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.MAP, 9)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.content))
            for kiter201, viter202 in self.content.items():
                oprot.writeString(kiter201.encode('utf-8') if sys.version_info[0] == 2 else kiter201)
                oprot.writeString(viter202.encode('utf-8') if sys.version_info[0] == 2 else viter202)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class NotificationFetchResult(object):
    """
    Attributes:
     - fetchMode
     - itemList
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'fetchMode', None, None, ),  # 1
        (2, TType.LIST, 'itemList', (TType.STRUCT, (NotificationItem, NotificationItem.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, fetchMode=None, itemList=None,):
        self.fetchMode = fetchMode
        self.itemList = itemList

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.fetchMode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.itemList = []
                    (_etype206, _size203) = iprot.readListBegin()
                    for _i207 in range(_size203):
                        _elem208 = NotificationItem()
                        _elem208.read(iprot)
                        self.itemList.append(_elem208)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('NotificationFetchResult')
        if self.fetchMode is not None:
            oprot.writeFieldBegin('fetchMode', TType.I32, 1)
            oprot.writeI32(self.fetchMode)
            oprot.writeFieldEnd()
        if self.itemList is not None:
            oprot.writeFieldBegin('itemList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.itemList))
            for iter209 in self.itemList:
                iter209.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Operation(object):
    """
    Attributes:
     - revision
     - createdTime
     - type
     - reqSeq
     - checksum
     - status
     - param1
     - param2
     - param3
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'revision', None, None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        (3, TType.I32, 'type', None, None, ),  # 3
        (4, TType.I32, 'reqSeq', None, None, ),  # 4
        (5, TType.STRING, 'checksum', 'UTF8', None, ),  # 5
        None,  # 6
        (7, TType.I32, 'status', None, None, ),  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'param1', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'param2', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'param3', 'UTF8', None, ),  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        (20, TType.STRUCT, 'message', (Message, Message.thrift_spec), None, ),  # 20
    )

    def __init__(self, revision=None, createdTime=None, type=None, reqSeq=None, checksum=None, status=None, param1=None, param2=None, param3=None, message=None,):
        self.revision = revision
        self.createdTime = createdTime
        self.type = type
        self.reqSeq = reqSeq
        self.checksum = checksum
        self.status = status
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.revision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.reqSeq = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.checksum = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.param1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.param2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.param3 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Operation')
        if self.revision is not None:
            oprot.writeFieldBegin('revision', TType.I64, 1)
            oprot.writeI64(self.revision)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.reqSeq is not None:
            oprot.writeFieldBegin('reqSeq', TType.I32, 4)
            oprot.writeI32(self.reqSeq)
            oprot.writeFieldEnd()
        if self.checksum is not None:
            oprot.writeFieldBegin('checksum', TType.STRING, 5)
            oprot.writeString(self.checksum.encode('utf-8') if sys.version_info[0] == 2 else self.checksum)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 7)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.param1 is not None:
            oprot.writeFieldBegin('param1', TType.STRING, 10)
            oprot.writeString(self.param1.encode('utf-8') if sys.version_info[0] == 2 else self.param1)
            oprot.writeFieldEnd()
        if self.param2 is not None:
            oprot.writeFieldBegin('param2', TType.STRING, 11)
            oprot.writeString(self.param2.encode('utf-8') if sys.version_info[0] == 2 else self.param2)
            oprot.writeFieldEnd()
        if self.param3 is not None:
            oprot.writeFieldBegin('param3', TType.STRING, 12)
            oprot.writeString(self.param3.encode('utf-8') if sys.version_info[0] == 2 else self.param3)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 20)
            self.message.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PaymentReservation(object):
    """
    Attributes:
     - receiverMid
     - productId
     - language
     - location
     - currency
     - price
     - appStoreCode
     - messageText
     - messageTemplate
     - packageId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'receiverMid', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'productId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'location', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'currency', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'price', 'UTF8', None, ),  # 6
        (7, TType.I32, 'appStoreCode', None, None, ),  # 7
        (8, TType.STRING, 'messageText', 'UTF8', None, ),  # 8
        (9, TType.I32, 'messageTemplate', None, None, ),  # 9
        (10, TType.I64, 'packageId', None, None, ),  # 10
    )

    def __init__(self, receiverMid=None, productId=None, language=None, location=None, currency=None, price=None, appStoreCode=None, messageText=None, messageTemplate=None, packageId=None,):
        self.receiverMid = receiverMid
        self.productId = productId
        self.language = language
        self.location = location
        self.currency = currency
        self.price = price
        self.appStoreCode = appStoreCode
        self.messageText = messageText
        self.messageTemplate = messageTemplate
        self.packageId = packageId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.receiverMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.location = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.messageText = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.messageTemplate = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('PaymentReservation')
        if self.receiverMid is not None:
            oprot.writeFieldBegin('receiverMid', TType.STRING, 1)
            oprot.writeString(self.receiverMid.encode('utf-8') if sys.version_info[0] == 2 else self.receiverMid)
            oprot.writeFieldEnd()
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 2)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.location is not None:
            oprot.writeFieldBegin('location', TType.STRING, 4)
            oprot.writeString(self.location.encode('utf-8') if sys.version_info[0] == 2 else self.location)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 5)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 6)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 7)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.messageText is not None:
            oprot.writeFieldBegin('messageText', TType.STRING, 8)
            oprot.writeString(self.messageText.encode('utf-8') if sys.version_info[0] == 2 else self.messageText)
            oprot.writeFieldEnd()
        if self.messageTemplate is not None:
            oprot.writeFieldBegin('messageTemplate', TType.I32, 9)
            oprot.writeI32(self.messageTemplate)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 10)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PaymentReservationResult(object):
    """
    Attributes:
     - orderId
     - confirmUrl
     - extras
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'orderId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'confirmUrl', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'extras', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, orderId=None, confirmUrl=None, extras=None,):
        self.orderId = orderId
        self.confirmUrl = confirmUrl
        self.extras = extras

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.orderId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.confirmUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.extras = {}
                    (_ktype211, _vtype212, _size210) = iprot.readMapBegin()
                    for _i214 in range(_size210):
                        _key215 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val216 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.extras[_key215] = _val216
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('PaymentReservationResult')
        if self.orderId is not None:
            oprot.writeFieldBegin('orderId', TType.STRING, 1)
            oprot.writeString(self.orderId.encode('utf-8') if sys.version_info[0] == 2 else self.orderId)
            oprot.writeFieldEnd()
        if self.confirmUrl is not None:
            oprot.writeFieldBegin('confirmUrl', TType.STRING, 2)
            oprot.writeString(self.confirmUrl.encode('utf-8') if sys.version_info[0] == 2 else self.confirmUrl)
            oprot.writeFieldEnd()
        if self.extras is not None:
            oprot.writeFieldBegin('extras', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.extras))
            for kiter217, viter218 in self.extras.items():
                oprot.writeString(kiter217.encode('utf-8') if sys.version_info[0] == 2 else kiter217)
                oprot.writeString(viter218.encode('utf-8') if sys.version_info[0] == 2 else viter218)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Product(object):
    """
    Attributes:
     - productId
     - packageId
     - version
     - authorName
     - onSale
     - validDays
     - saleType
     - copyright
     - title
     - descriptionText
     - shopOrderId
     - fromMid
     - toMid
     - validUntil
     - priceTier
     - price
     - currency
     - currencySymbol
     - paymentType
     - createDate
     - ownFlag
     - eventType
     - urlSchema
     - downloadUrl
     - buddyMid
     - publishSince
     - newFlag
     - missionFlag
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'productId', 'UTF8', None, ),  # 1
        (2, TType.I64, 'packageId', None, None, ),  # 2
        (3, TType.I32, 'version', None, None, ),  # 3
        (4, TType.STRING, 'authorName', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'onSale', None, None, ),  # 5
        (6, TType.I32, 'validDays', None, None, ),  # 6
        (7, TType.I32, 'saleType', None, None, ),  # 7
        (8, TType.STRING, 'copyright', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'title', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'descriptionText', 'UTF8', None, ),  # 10
        (11, TType.I64, 'shopOrderId', None, None, ),  # 11
        (12, TType.STRING, 'fromMid', 'UTF8', None, ),  # 12
        (13, TType.STRING, 'toMid', 'UTF8', None, ),  # 13
        (14, TType.I64, 'validUntil', None, None, ),  # 14
        (15, TType.I32, 'priceTier', None, None, ),  # 15
        (16, TType.STRING, 'price', 'UTF8', None, ),  # 16
        (17, TType.STRING, 'currency', 'UTF8', None, ),  # 17
        (18, TType.STRING, 'currencySymbol', 'UTF8', None, ),  # 18
        (19, TType.I32, 'paymentType', None, None, ),  # 19
        (20, TType.I64, 'createDate', None, None, ),  # 20
        (21, TType.BOOL, 'ownFlag', None, None, ),  # 21
        (22, TType.I32, 'eventType', None, None, ),  # 22
        (23, TType.STRING, 'urlSchema', 'UTF8', None, ),  # 23
        (24, TType.STRING, 'downloadUrl', 'UTF8', None, ),  # 24
        (25, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 25
        (26, TType.I64, 'publishSince', None, None, ),  # 26
        (27, TType.BOOL, 'newFlag', None, None, ),  # 27
        (28, TType.BOOL, 'missionFlag', None, None, ),  # 28
    )

    def __init__(self, productId=None, packageId=None, version=None, authorName=None, onSale=None, validDays=None, saleType=None, copyright=None, title=None, descriptionText=None, shopOrderId=None, fromMid=None, toMid=None, validUntil=None, priceTier=None, price=None, currency=None, currencySymbol=None, paymentType=None, createDate=None, ownFlag=None, eventType=None, urlSchema=None, downloadUrl=None, buddyMid=None, publishSince=None, newFlag=None, missionFlag=None,):
        self.productId = productId
        self.packageId = packageId
        self.version = version
        self.authorName = authorName
        self.onSale = onSale
        self.validDays = validDays
        self.saleType = saleType
        self.copyright = copyright
        self.title = title
        self.descriptionText = descriptionText
        self.shopOrderId = shopOrderId
        self.fromMid = fromMid
        self.toMid = toMid
        self.validUntil = validUntil
        self.priceTier = priceTier
        self.price = price
        self.currency = currency
        self.currencySymbol = currencySymbol
        self.paymentType = paymentType
        self.createDate = createDate
        self.ownFlag = ownFlag
        self.eventType = eventType
        self.urlSchema = urlSchema
        self.downloadUrl = downloadUrl
        self.buddyMid = buddyMid
        self.publishSince = publishSince
        self.newFlag = newFlag
        self.missionFlag = missionFlag

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.authorName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.onSale = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.validDays = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.saleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.copyright = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.descriptionText = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.shopOrderId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.fromMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.toMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.validUntil = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.priceTier = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRING:
                    self.currencySymbol = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I32:
                    self.paymentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I64:
                    self.createDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.BOOL:
                    self.ownFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.I32:
                    self.eventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.urlSchema = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRING:
                    self.downloadUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRING:
                    self.buddyMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.I64:
                    self.publishSince = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.BOOL:
                    self.newFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.BOOL:
                    self.missionFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Product')
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 1)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 2)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 3)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.authorName is not None:
            oprot.writeFieldBegin('authorName', TType.STRING, 4)
            oprot.writeString(self.authorName.encode('utf-8') if sys.version_info[0] == 2 else self.authorName)
            oprot.writeFieldEnd()
        if self.onSale is not None:
            oprot.writeFieldBegin('onSale', TType.BOOL, 5)
            oprot.writeBool(self.onSale)
            oprot.writeFieldEnd()
        if self.validDays is not None:
            oprot.writeFieldBegin('validDays', TType.I32, 6)
            oprot.writeI32(self.validDays)
            oprot.writeFieldEnd()
        if self.saleType is not None:
            oprot.writeFieldBegin('saleType', TType.I32, 7)
            oprot.writeI32(self.saleType)
            oprot.writeFieldEnd()
        if self.copyright is not None:
            oprot.writeFieldBegin('copyright', TType.STRING, 8)
            oprot.writeString(self.copyright.encode('utf-8') if sys.version_info[0] == 2 else self.copyright)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 9)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.descriptionText is not None:
            oprot.writeFieldBegin('descriptionText', TType.STRING, 10)
            oprot.writeString(self.descriptionText.encode('utf-8') if sys.version_info[0] == 2 else self.descriptionText)
            oprot.writeFieldEnd()
        if self.shopOrderId is not None:
            oprot.writeFieldBegin('shopOrderId', TType.I64, 11)
            oprot.writeI64(self.shopOrderId)
            oprot.writeFieldEnd()
        if self.fromMid is not None:
            oprot.writeFieldBegin('fromMid', TType.STRING, 12)
            oprot.writeString(self.fromMid.encode('utf-8') if sys.version_info[0] == 2 else self.fromMid)
            oprot.writeFieldEnd()
        if self.toMid is not None:
            oprot.writeFieldBegin('toMid', TType.STRING, 13)
            oprot.writeString(self.toMid.encode('utf-8') if sys.version_info[0] == 2 else self.toMid)
            oprot.writeFieldEnd()
        if self.validUntil is not None:
            oprot.writeFieldBegin('validUntil', TType.I64, 14)
            oprot.writeI64(self.validUntil)
            oprot.writeFieldEnd()
        if self.priceTier is not None:
            oprot.writeFieldBegin('priceTier', TType.I32, 15)
            oprot.writeI32(self.priceTier)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 16)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 17)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.currencySymbol is not None:
            oprot.writeFieldBegin('currencySymbol', TType.STRING, 18)
            oprot.writeString(self.currencySymbol.encode('utf-8') if sys.version_info[0] == 2 else self.currencySymbol)
            oprot.writeFieldEnd()
        if self.paymentType is not None:
            oprot.writeFieldBegin('paymentType', TType.I32, 19)
            oprot.writeI32(self.paymentType)
            oprot.writeFieldEnd()
        if self.createDate is not None:
            oprot.writeFieldBegin('createDate', TType.I64, 20)
            oprot.writeI64(self.createDate)
            oprot.writeFieldEnd()
        if self.ownFlag is not None:
            oprot.writeFieldBegin('ownFlag', TType.BOOL, 21)
            oprot.writeBool(self.ownFlag)
            oprot.writeFieldEnd()
        if self.eventType is not None:
            oprot.writeFieldBegin('eventType', TType.I32, 22)
            oprot.writeI32(self.eventType)
            oprot.writeFieldEnd()
        if self.urlSchema is not None:
            oprot.writeFieldBegin('urlSchema', TType.STRING, 23)
            oprot.writeString(self.urlSchema.encode('utf-8') if sys.version_info[0] == 2 else self.urlSchema)
            oprot.writeFieldEnd()
        if self.downloadUrl is not None:
            oprot.writeFieldBegin('downloadUrl', TType.STRING, 24)
            oprot.writeString(self.downloadUrl.encode('utf-8') if sys.version_info[0] == 2 else self.downloadUrl)
            oprot.writeFieldEnd()
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 25)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.publishSince is not None:
            oprot.writeFieldBegin('publishSince', TType.I64, 26)
            oprot.writeI64(self.publishSince)
            oprot.writeFieldEnd()
        if self.newFlag is not None:
            oprot.writeFieldBegin('newFlag', TType.BOOL, 27)
            oprot.writeBool(self.newFlag)
            oprot.writeFieldEnd()
        if self.missionFlag is not None:
            oprot.writeFieldBegin('missionFlag', TType.BOOL, 28)
            oprot.writeBool(self.missionFlag)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ProductList(object):
    """
    Attributes:
     - hasNext
     - bannerSequence
     - bannerTargetType
     - bannerTargetPath
     - productList
     - bannerLang
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'hasNext', None, None, ),  # 1
        None,  # 2
        None,  # 3
        (4, TType.I64, 'bannerSequence', None, None, ),  # 4
        (5, TType.I32, 'bannerTargetType', None, None, ),  # 5
        (6, TType.STRING, 'bannerTargetPath', 'UTF8', None, ),  # 6
        (7, TType.LIST, 'productList', (TType.STRUCT, (Product, Product.thrift_spec), False), None, ),  # 7
        (8, TType.STRING, 'bannerLang', 'UTF8', None, ),  # 8
    )

    def __init__(self, hasNext=None, bannerSequence=None, bannerTargetType=None, bannerTargetPath=None, productList=None, bannerLang=None,):
        self.hasNext = hasNext
        self.bannerSequence = bannerSequence
        self.bannerTargetType = bannerTargetType
        self.bannerTargetPath = bannerTargetPath
        self.productList = productList
        self.bannerLang = bannerLang

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.hasNext = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.bannerSequence = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.bannerTargetType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.bannerTargetPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.productList = []
                    (_etype222, _size219) = iprot.readListBegin()
                    for _i223 in range(_size219):
                        _elem224 = Product()
                        _elem224.read(iprot)
                        self.productList.append(_elem224)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.bannerLang = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ProductList')
        if self.hasNext is not None:
            oprot.writeFieldBegin('hasNext', TType.BOOL, 1)
            oprot.writeBool(self.hasNext)
            oprot.writeFieldEnd()
        if self.bannerSequence is not None:
            oprot.writeFieldBegin('bannerSequence', TType.I64, 4)
            oprot.writeI64(self.bannerSequence)
            oprot.writeFieldEnd()
        if self.bannerTargetType is not None:
            oprot.writeFieldBegin('bannerTargetType', TType.I32, 5)
            oprot.writeI32(self.bannerTargetType)
            oprot.writeFieldEnd()
        if self.bannerTargetPath is not None:
            oprot.writeFieldBegin('bannerTargetPath', TType.STRING, 6)
            oprot.writeString(self.bannerTargetPath.encode('utf-8') if sys.version_info[0] == 2 else self.bannerTargetPath)
            oprot.writeFieldEnd()
        if self.productList is not None:
            oprot.writeFieldBegin('productList', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.productList))
            for iter225 in self.productList:
                iter225.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.bannerLang is not None:
            oprot.writeFieldBegin('bannerLang', TType.STRING, 8)
            oprot.writeString(self.bannerLang.encode('utf-8') if sys.version_info[0] == 2 else self.bannerLang)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ProductSimple(object):
    """
    Attributes:
     - productId
     - packageId
     - version
     - onSale
     - validUntil
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'productId', 'UTF8', None, ),  # 1
        (2, TType.I64, 'packageId', None, None, ),  # 2
        (3, TType.I32, 'version', None, None, ),  # 3
        (4, TType.BOOL, 'onSale', None, None, ),  # 4
        (5, TType.I64, 'validUntil', None, None, ),  # 5
    )

    def __init__(self, productId=None, packageId=None, version=None, onSale=None, validUntil=None,):
        self.productId = productId
        self.packageId = packageId
        self.version = version
        self.onSale = onSale
        self.validUntil = validUntil

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.onSale = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.validUntil = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ProductSimple')
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 1)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 2)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 3)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.onSale is not None:
            oprot.writeFieldBegin('onSale', TType.BOOL, 4)
            oprot.writeBool(self.onSale)
            oprot.writeFieldEnd()
        if self.validUntil is not None:
            oprot.writeFieldBegin('validUntil', TType.I64, 5)
            oprot.writeI64(self.validUntil)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ProductSimpleList(object):
    """
    Attributes:
     - hasNext
     - reinvokeHour
     - lastVersionSeq
     - productList
     - recentNewReleaseDate
     - recentEventReleaseDate
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'hasNext', None, None, ),  # 1
        (2, TType.I32, 'reinvokeHour', None, None, ),  # 2
        (3, TType.I64, 'lastVersionSeq', None, None, ),  # 3
        (4, TType.LIST, 'productList', (TType.STRUCT, (ProductSimple, ProductSimple.thrift_spec), False), None, ),  # 4
        (5, TType.I64, 'recentNewReleaseDate', None, None, ),  # 5
        (6, TType.I64, 'recentEventReleaseDate', None, None, ),  # 6
    )

    def __init__(self, hasNext=None, reinvokeHour=None, lastVersionSeq=None, productList=None, recentNewReleaseDate=None, recentEventReleaseDate=None,):
        self.hasNext = hasNext
        self.reinvokeHour = reinvokeHour
        self.lastVersionSeq = lastVersionSeq
        self.productList = productList
        self.recentNewReleaseDate = recentNewReleaseDate
        self.recentEventReleaseDate = recentEventReleaseDate

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.hasNext = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.reinvokeHour = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.lastVersionSeq = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.productList = []
                    (_etype229, _size226) = iprot.readListBegin()
                    for _i230 in range(_size226):
                        _elem231 = ProductSimple()
                        _elem231.read(iprot)
                        self.productList.append(_elem231)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.recentNewReleaseDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.recentEventReleaseDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ProductSimpleList')
        if self.hasNext is not None:
            oprot.writeFieldBegin('hasNext', TType.BOOL, 1)
            oprot.writeBool(self.hasNext)
            oprot.writeFieldEnd()
        if self.reinvokeHour is not None:
            oprot.writeFieldBegin('reinvokeHour', TType.I32, 2)
            oprot.writeI32(self.reinvokeHour)
            oprot.writeFieldEnd()
        if self.lastVersionSeq is not None:
            oprot.writeFieldBegin('lastVersionSeq', TType.I64, 3)
            oprot.writeI64(self.lastVersionSeq)
            oprot.writeFieldEnd()
        if self.productList is not None:
            oprot.writeFieldBegin('productList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.productList))
            for iter232 in self.productList:
                iter232.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.recentNewReleaseDate is not None:
            oprot.writeFieldBegin('recentNewReleaseDate', TType.I64, 5)
            oprot.writeI64(self.recentNewReleaseDate)
            oprot.writeFieldEnd()
        if self.recentEventReleaseDate is not None:
            oprot.writeFieldBegin('recentEventReleaseDate', TType.I64, 6)
            oprot.writeI64(self.recentEventReleaseDate)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Profile(object):
    """
    Attributes:
     - mid
     - userid
     - phone
     - email
     - regionCode
     - displayName
     - phoneticName
     - pictureStatus
     - thumbnailUrl
     - statusMessage
     - allowSearchByUserid
     - allowSearchByEmail
     - picturePath
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        None,  # 2
        (3, TType.STRING, 'userid', 'UTF8', None, ),  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'phone', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'email', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'regionCode', 'UTF8', None, ),  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        (20, TType.STRING, 'displayName', 'UTF8', None, ),  # 20
        (21, TType.STRING, 'phoneticName', 'UTF8', None, ),  # 21
        (22, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 22
        (23, TType.STRING, 'thumbnailUrl', 'UTF8', None, ),  # 23
        (24, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 24
        None,  # 25
        None,  # 26
        None,  # 27
        None,  # 28
        None,  # 29
        None,  # 30
        (31, TType.BOOL, 'allowSearchByUserid', None, None, ),  # 31
        (32, TType.BOOL, 'allowSearchByEmail', None, None, ),  # 32
        (33, TType.STRING, 'picturePath', 'UTF8', None, ),  # 33
    )

    def __init__(self, mid=None, userid=None, phone=None, email=None, regionCode=None, displayName=None, phoneticName=None, pictureStatus=None, thumbnailUrl=None, statusMessage=None, allowSearchByUserid=None, allowSearchByEmail=None, picturePath=None,):
        self.mid = mid
        self.userid = userid
        self.phone = phone
        self.email = email
        self.regionCode = regionCode
        self.displayName = displayName
        self.phoneticName = phoneticName
        self.pictureStatus = pictureStatus
        self.thumbnailUrl = thumbnailUrl
        self.statusMessage = statusMessage
        self.allowSearchByUserid = allowSearchByUserid
        self.allowSearchByEmail = allowSearchByEmail
        self.picturePath = picturePath

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.userid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.phone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.regionCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRING:
                    self.phoneticName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.allowSearchByUserid = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 32:
                if ftype == TType.BOOL:
                    self.allowSearchByEmail = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 33:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Profile')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.userid is not None:
            oprot.writeFieldBegin('userid', TType.STRING, 3)
            oprot.writeString(self.userid.encode('utf-8') if sys.version_info[0] == 2 else self.userid)
            oprot.writeFieldEnd()
        if self.phone is not None:
            oprot.writeFieldBegin('phone', TType.STRING, 10)
            oprot.writeString(self.phone.encode('utf-8') if sys.version_info[0] == 2 else self.phone)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 11)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.regionCode is not None:
            oprot.writeFieldBegin('regionCode', TType.STRING, 12)
            oprot.writeString(self.regionCode.encode('utf-8') if sys.version_info[0] == 2 else self.regionCode)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 20)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.phoneticName is not None:
            oprot.writeFieldBegin('phoneticName', TType.STRING, 21)
            oprot.writeString(self.phoneticName.encode('utf-8') if sys.version_info[0] == 2 else self.phoneticName)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 22)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 23)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 24)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.allowSearchByUserid is not None:
            oprot.writeFieldBegin('allowSearchByUserid', TType.BOOL, 31)
            oprot.writeBool(self.allowSearchByUserid)
            oprot.writeFieldEnd()
        if self.allowSearchByEmail is not None:
            oprot.writeFieldBegin('allowSearchByEmail', TType.BOOL, 32)
            oprot.writeBool(self.allowSearchByEmail)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 33)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ProximityMatchCandidateResult(object):
    """
    Attributes:
     - users
     - buddies
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'users', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 1
        (2, TType.LIST, 'buddies', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, users=None, buddies=None,):
        self.users = users
        self.buddies = buddies

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.users = []
                    (_etype236, _size233) = iprot.readListBegin()
                    for _i237 in range(_size233):
                        _elem238 = Contact()
                        _elem238.read(iprot)
                        self.users.append(_elem238)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.buddies = []
                    (_etype242, _size239) = iprot.readListBegin()
                    for _i243 in range(_size239):
                        _elem244 = Contact()
                        _elem244.read(iprot)
                        self.buddies.append(_elem244)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ProximityMatchCandidateResult')
        if self.users is not None:
            oprot.writeFieldBegin('users', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.users))
            for iter245 in self.users:
                iter245.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.buddies is not None:
            oprot.writeFieldBegin('buddies', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.buddies))
            for iter246 in self.buddies:
                iter246.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RegisterWithSnsIdResult(object):
    """
    Attributes:
     - authToken
     - userCreated
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'authToken', 'UTF8', None, ),  # 1
        (2, TType.BOOL, 'userCreated', None, None, ),  # 2
    )

    def __init__(self, authToken=None, userCreated=None,):
        self.authToken = authToken
        self.userCreated = userCreated

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.authToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.userCreated = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('RegisterWithSnsIdResult')
        if self.authToken is not None:
            oprot.writeFieldBegin('authToken', TType.STRING, 1)
            oprot.writeString(self.authToken.encode('utf-8') if sys.version_info[0] == 2 else self.authToken)
            oprot.writeFieldEnd()
        if self.userCreated is not None:
            oprot.writeFieldBegin('userCreated', TType.BOOL, 2)
            oprot.writeBool(self.userCreated)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RequestTokenResponse(object):
    """
    Attributes:
     - requestToken
     - returnUrl
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'requestToken', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'returnUrl', 'UTF8', None, ),  # 2
    )

    def __init__(self, requestToken=None, returnUrl=None,):
        self.requestToken = requestToken
        self.returnUrl = returnUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.requestToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.returnUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('RequestTokenResponse')
        if self.requestToken is not None:
            oprot.writeFieldBegin('requestToken', TType.STRING, 1)
            oprot.writeString(self.requestToken.encode('utf-8') if sys.version_info[0] == 2 else self.requestToken)
            oprot.writeFieldEnd()
        if self.returnUrl is not None:
            oprot.writeFieldBegin('returnUrl', TType.STRING, 2)
            oprot.writeString(self.returnUrl.encode('utf-8') if sys.version_info[0] == 2 else self.returnUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Room(object):
    """
    Attributes:
     - mid
     - createdTime
     - contacts
     - notificationDisabled
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.I64, 'createdTime', None, None, ),  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.LIST, 'contacts', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 10
        None,  # 11
        None,  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        None,  # 21
        None,  # 22
        None,  # 23
        None,  # 24
        None,  # 25
        None,  # 26
        None,  # 27
        None,  # 28
        None,  # 29
        None,  # 30
        (31, TType.BOOL, 'notificationDisabled', None, None, ),  # 31
    )

    def __init__(self, mid=None, createdTime=None, contacts=None, notificationDisabled=None,):
        self.mid = mid
        self.createdTime = createdTime
        self.contacts = contacts
        self.notificationDisabled = notificationDisabled

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.createdTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.contacts = []
                    (_etype250, _size247) = iprot.readListBegin()
                    for _i251 in range(_size247):
                        _elem252 = Contact()
                        _elem252.read(iprot)
                        self.contacts.append(_elem252)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 31:
                if ftype == TType.BOOL:
                    self.notificationDisabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Room')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.createdTime is not None:
            oprot.writeFieldBegin('createdTime', TType.I64, 2)
            oprot.writeI64(self.createdTime)
            oprot.writeFieldEnd()
        if self.contacts is not None:
            oprot.writeFieldBegin('contacts', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.contacts))
            for iter253 in self.contacts:
                iter253.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.notificationDisabled is not None:
            oprot.writeFieldBegin('notificationDisabled', TType.BOOL, 31)
            oprot.writeBool(self.notificationDisabled)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RSAKey(object):
    """
    Attributes:
     - keynm
     - nvalue
     - evalue
     - sessionKey
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'keynm', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'nvalue', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'evalue', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'sessionKey', 'UTF8', None, ),  # 4
    )

    def __init__(self, keynm=None, nvalue=None, evalue=None, sessionKey=None,):
        self.keynm = keynm
        self.nvalue = nvalue
        self.evalue = evalue
        self.sessionKey = sessionKey

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.keynm = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.nvalue = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.evalue = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.sessionKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('RSAKey')
        if self.keynm is not None:
            oprot.writeFieldBegin('keynm', TType.STRING, 1)
            oprot.writeString(self.keynm.encode('utf-8') if sys.version_info[0] == 2 else self.keynm)
            oprot.writeFieldEnd()
        if self.nvalue is not None:
            oprot.writeFieldBegin('nvalue', TType.STRING, 2)
            oprot.writeString(self.nvalue.encode('utf-8') if sys.version_info[0] == 2 else self.nvalue)
            oprot.writeFieldEnd()
        if self.evalue is not None:
            oprot.writeFieldBegin('evalue', TType.STRING, 3)
            oprot.writeString(self.evalue.encode('utf-8') if sys.version_info[0] == 2 else self.evalue)
            oprot.writeFieldEnd()
        if self.sessionKey is not None:
            oprot.writeFieldBegin('sessionKey', TType.STRING, 4)
            oprot.writeString(self.sessionKey.encode('utf-8') if sys.version_info[0] == 2 else self.sessionKey)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SendBuddyMessageResult(object):
    """
    Attributes:
     - requestId
     - state
     - messageId
     - eventNo
     - receiverCount
     - successCount
     - failCount
     - cancelCount
     - blockCount
     - unregisterCount
     - timestamp
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'state', None, None, ),  # 2
        (3, TType.STRING, 'messageId', 'UTF8', None, ),  # 3
        (4, TType.I32, 'eventNo', None, None, ),  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.I64, 'receiverCount', None, None, ),  # 11
        (12, TType.I64, 'successCount', None, None, ),  # 12
        (13, TType.I64, 'failCount', None, None, ),  # 13
        (14, TType.I64, 'cancelCount', None, None, ),  # 14
        (15, TType.I64, 'blockCount', None, None, ),  # 15
        (16, TType.I64, 'unregisterCount', None, None, ),  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        (21, TType.I64, 'timestamp', None, None, ),  # 21
        (22, TType.STRING, 'message', 'UTF8', None, ),  # 22
    )

    def __init__(self, requestId=None, state=None, messageId=None, eventNo=None, receiverCount=None, successCount=None, failCount=None, cancelCount=None, blockCount=None, unregisterCount=None, timestamp=None, message=None,):
        self.requestId = requestId
        self.state = state
        self.messageId = messageId
        self.eventNo = eventNo
        self.receiverCount = receiverCount
        self.successCount = successCount
        self.failCount = failCount
        self.cancelCount = cancelCount
        self.blockCount = blockCount
        self.unregisterCount = unregisterCount
        self.timestamp = timestamp
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.messageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.eventNo = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.receiverCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.successCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.failCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.cancelCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I64:
                    self.blockCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I64:
                    self.unregisterCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SendBuddyMessageResult')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.state is not None:
            oprot.writeFieldBegin('state', TType.I32, 2)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.messageId is not None:
            oprot.writeFieldBegin('messageId', TType.STRING, 3)
            oprot.writeString(self.messageId.encode('utf-8') if sys.version_info[0] == 2 else self.messageId)
            oprot.writeFieldEnd()
        if self.eventNo is not None:
            oprot.writeFieldBegin('eventNo', TType.I32, 4)
            oprot.writeI32(self.eventNo)
            oprot.writeFieldEnd()
        if self.receiverCount is not None:
            oprot.writeFieldBegin('receiverCount', TType.I64, 11)
            oprot.writeI64(self.receiverCount)
            oprot.writeFieldEnd()
        if self.successCount is not None:
            oprot.writeFieldBegin('successCount', TType.I64, 12)
            oprot.writeI64(self.successCount)
            oprot.writeFieldEnd()
        if self.failCount is not None:
            oprot.writeFieldBegin('failCount', TType.I64, 13)
            oprot.writeI64(self.failCount)
            oprot.writeFieldEnd()
        if self.cancelCount is not None:
            oprot.writeFieldBegin('cancelCount', TType.I64, 14)
            oprot.writeI64(self.cancelCount)
            oprot.writeFieldEnd()
        if self.blockCount is not None:
            oprot.writeFieldBegin('blockCount', TType.I64, 15)
            oprot.writeI64(self.blockCount)
            oprot.writeFieldEnd()
        if self.unregisterCount is not None:
            oprot.writeFieldBegin('unregisterCount', TType.I64, 16)
            oprot.writeI64(self.unregisterCount)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 21)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 22)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SetBuddyOnAirResult(object):
    """
    Attributes:
     - requestId
     - state
     - eventNo
     - receiverCount
     - successCount
     - failCount
     - cancelCount
     - unregisterCount
     - timestamp
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'state', None, None, ),  # 2
        (3, TType.I32, 'eventNo', None, None, ),  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.I64, 'receiverCount', None, None, ),  # 11
        (12, TType.I64, 'successCount', None, None, ),  # 12
        (13, TType.I64, 'failCount', None, None, ),  # 13
        (14, TType.I64, 'cancelCount', None, None, ),  # 14
        (15, TType.I64, 'unregisterCount', None, None, ),  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        (21, TType.I64, 'timestamp', None, None, ),  # 21
        (22, TType.STRING, 'message', 'UTF8', None, ),  # 22
    )

    def __init__(self, requestId=None, state=None, eventNo=None, receiverCount=None, successCount=None, failCount=None, cancelCount=None, unregisterCount=None, timestamp=None, message=None,):
        self.requestId = requestId
        self.state = state
        self.eventNo = eventNo
        self.receiverCount = receiverCount
        self.successCount = successCount
        self.failCount = failCount
        self.cancelCount = cancelCount
        self.unregisterCount = unregisterCount
        self.timestamp = timestamp
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eventNo = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.receiverCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.successCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.failCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.cancelCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I64:
                    self.unregisterCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SetBuddyOnAirResult')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.state is not None:
            oprot.writeFieldBegin('state', TType.I32, 2)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.eventNo is not None:
            oprot.writeFieldBegin('eventNo', TType.I32, 3)
            oprot.writeI32(self.eventNo)
            oprot.writeFieldEnd()
        if self.receiverCount is not None:
            oprot.writeFieldBegin('receiverCount', TType.I64, 11)
            oprot.writeI64(self.receiverCount)
            oprot.writeFieldEnd()
        if self.successCount is not None:
            oprot.writeFieldBegin('successCount', TType.I64, 12)
            oprot.writeI64(self.successCount)
            oprot.writeFieldEnd()
        if self.failCount is not None:
            oprot.writeFieldBegin('failCount', TType.I64, 13)
            oprot.writeI64(self.failCount)
            oprot.writeFieldEnd()
        if self.cancelCount is not None:
            oprot.writeFieldBegin('cancelCount', TType.I64, 14)
            oprot.writeI64(self.cancelCount)
            oprot.writeFieldEnd()
        if self.unregisterCount is not None:
            oprot.writeFieldBegin('unregisterCount', TType.I64, 15)
            oprot.writeI64(self.unregisterCount)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 21)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 22)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Settings(object):
    """
    Attributes:
     - notificationEnable
     - notificationMuteExpiration
     - notificationNewMessage
     - notificationGroupInvitation
     - notificationShowMessage
     - notificationIncomingCall
     - notificationSoundMessage
     - notificationSoundGroup
     - notificationDisabledWithSub
     - privacySyncContacts
     - privacySearchByPhoneNumber
     - privacySearchByUserid
     - privacySearchByEmail
     - privacyAllowSecondaryDeviceLogin
     - privacyProfileImagePostToMyhome
     - privacyReceiveMessagesFromNotFriend
     - contactMyTicket
     - identityProvider
     - identityIdentifier
     - snsAccounts
     - phoneRegistration
     - emailConfirmationStatus
     - preferenceLocale
     - customModes
    """

    thrift_spec = (
        None,  # 0
        None,  # 1
        None,  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.BOOL, 'notificationEnable', None, None, ),  # 10
        (11, TType.I64, 'notificationMuteExpiration', None, None, ),  # 11
        (12, TType.BOOL, 'notificationNewMessage', None, None, ),  # 12
        (13, TType.BOOL, 'notificationGroupInvitation', None, None, ),  # 13
        (14, TType.BOOL, 'notificationShowMessage', None, None, ),  # 14
        (15, TType.BOOL, 'notificationIncomingCall', None, None, ),  # 15
        (16, TType.STRING, 'notificationSoundMessage', 'UTF8', None, ),  # 16
        (17, TType.STRING, 'notificationSoundGroup', 'UTF8', None, ),  # 17
        (18, TType.BOOL, 'notificationDisabledWithSub', None, None, ),  # 18
        None,  # 19
        (20, TType.BOOL, 'privacySyncContacts', None, None, ),  # 20
        (21, TType.BOOL, 'privacySearchByPhoneNumber', None, None, ),  # 21
        (22, TType.BOOL, 'privacySearchByUserid', None, None, ),  # 22
        (23, TType.BOOL, 'privacySearchByEmail', None, None, ),  # 23
        (24, TType.BOOL, 'privacyAllowSecondaryDeviceLogin', None, None, ),  # 24
        (25, TType.BOOL, 'privacyProfileImagePostToMyhome', None, None, ),  # 25
        (26, TType.BOOL, 'privacyReceiveMessagesFromNotFriend', None, None, ),  # 26
        None,  # 27
        None,  # 28
        None,  # 29
        (30, TType.STRING, 'contactMyTicket', 'UTF8', None, ),  # 30
        None,  # 31
        None,  # 32
        None,  # 33
        None,  # 34
        None,  # 35
        None,  # 36
        None,  # 37
        None,  # 38
        None,  # 39
        (40, TType.I32, 'identityProvider', None, None, ),  # 40
        (41, TType.STRING, 'identityIdentifier', 'UTF8', None, ),  # 41
        (42, TType.MAP, 'snsAccounts', (TType.I32, None, TType.STRING, 'UTF8', False), None, ),  # 42
        (43, TType.BOOL, 'phoneRegistration', None, None, ),  # 43
        (44, TType.I32, 'emailConfirmationStatus', None, None, ),  # 44
        None,  # 45
        None,  # 46
        None,  # 47
        None,  # 48
        None,  # 49
        (50, TType.STRING, 'preferenceLocale', 'UTF8', None, ),  # 50
        None,  # 51
        None,  # 52
        None,  # 53
        None,  # 54
        None,  # 55
        None,  # 56
        None,  # 57
        None,  # 58
        None,  # 59
        (60, TType.MAP, 'customModes', (TType.I32, None, TType.STRING, 'UTF8', False), None, ),  # 60
    )

    def __init__(self, notificationEnable=None, notificationMuteExpiration=None, notificationNewMessage=None, notificationGroupInvitation=None, notificationShowMessage=None, notificationIncomingCall=None, notificationSoundMessage=None, notificationSoundGroup=None, notificationDisabledWithSub=None, privacySyncContacts=None, privacySearchByPhoneNumber=None, privacySearchByUserid=None, privacySearchByEmail=None, privacyAllowSecondaryDeviceLogin=None, privacyProfileImagePostToMyhome=None, privacyReceiveMessagesFromNotFriend=None, contactMyTicket=None, identityProvider=None, identityIdentifier=None, snsAccounts=None, phoneRegistration=None, emailConfirmationStatus=None, preferenceLocale=None, customModes=None,):
        self.notificationEnable = notificationEnable
        self.notificationMuteExpiration = notificationMuteExpiration
        self.notificationNewMessage = notificationNewMessage
        self.notificationGroupInvitation = notificationGroupInvitation
        self.notificationShowMessage = notificationShowMessage
        self.notificationIncomingCall = notificationIncomingCall
        self.notificationSoundMessage = notificationSoundMessage
        self.notificationSoundGroup = notificationSoundGroup
        self.notificationDisabledWithSub = notificationDisabledWithSub
        self.privacySyncContacts = privacySyncContacts
        self.privacySearchByPhoneNumber = privacySearchByPhoneNumber
        self.privacySearchByUserid = privacySearchByUserid
        self.privacySearchByEmail = privacySearchByEmail
        self.privacyAllowSecondaryDeviceLogin = privacyAllowSecondaryDeviceLogin
        self.privacyProfileImagePostToMyhome = privacyProfileImagePostToMyhome
        self.privacyReceiveMessagesFromNotFriend = privacyReceiveMessagesFromNotFriend
        self.contactMyTicket = contactMyTicket
        self.identityProvider = identityProvider
        self.identityIdentifier = identityIdentifier
        self.snsAccounts = snsAccounts
        self.phoneRegistration = phoneRegistration
        self.emailConfirmationStatus = emailConfirmationStatus
        self.preferenceLocale = preferenceLocale
        self.customModes = customModes

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 10:
                if ftype == TType.BOOL:
                    self.notificationEnable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.notificationMuteExpiration = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.BOOL:
                    self.notificationNewMessage = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.BOOL:
                    self.notificationGroupInvitation = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.BOOL:
                    self.notificationShowMessage = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.BOOL:
                    self.notificationIncomingCall = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.notificationSoundMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.notificationSoundGroup = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.BOOL:
                    self.notificationDisabledWithSub = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.BOOL:
                    self.privacySyncContacts = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.BOOL:
                    self.privacySearchByPhoneNumber = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.BOOL:
                    self.privacySearchByUserid = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.BOOL:
                    self.privacySearchByEmail = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.BOOL:
                    self.privacyAllowSecondaryDeviceLogin = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.BOOL:
                    self.privacyProfileImagePostToMyhome = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.BOOL:
                    self.privacyReceiveMessagesFromNotFriend = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 30:
                if ftype == TType.STRING:
                    self.contactMyTicket = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 40:
                if ftype == TType.I32:
                    self.identityProvider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 41:
                if ftype == TType.STRING:
                    self.identityIdentifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 42:
                if ftype == TType.MAP:
                    self.snsAccounts = {}
                    (_ktype255, _vtype256, _size254) = iprot.readMapBegin()
                    for _i258 in range(_size254):
                        _key259 = iprot.readI32()
                        _val260 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.snsAccounts[_key259] = _val260
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 43:
                if ftype == TType.BOOL:
                    self.phoneRegistration = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 44:
                if ftype == TType.I32:
                    self.emailConfirmationStatus = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 50:
                if ftype == TType.STRING:
                    self.preferenceLocale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 60:
                if ftype == TType.MAP:
                    self.customModes = {}
                    (_ktype262, _vtype263, _size261) = iprot.readMapBegin()
                    for _i265 in range(_size261):
                        _key266 = iprot.readI32()
                        _val267 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.customModes[_key266] = _val267
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Settings')
        if self.notificationEnable is not None:
            oprot.writeFieldBegin('notificationEnable', TType.BOOL, 10)
            oprot.writeBool(self.notificationEnable)
            oprot.writeFieldEnd()
        if self.notificationMuteExpiration is not None:
            oprot.writeFieldBegin('notificationMuteExpiration', TType.I64, 11)
            oprot.writeI64(self.notificationMuteExpiration)
            oprot.writeFieldEnd()
        if self.notificationNewMessage is not None:
            oprot.writeFieldBegin('notificationNewMessage', TType.BOOL, 12)
            oprot.writeBool(self.notificationNewMessage)
            oprot.writeFieldEnd()
        if self.notificationGroupInvitation is not None:
            oprot.writeFieldBegin('notificationGroupInvitation', TType.BOOL, 13)
            oprot.writeBool(self.notificationGroupInvitation)
            oprot.writeFieldEnd()
        if self.notificationShowMessage is not None:
            oprot.writeFieldBegin('notificationShowMessage', TType.BOOL, 14)
            oprot.writeBool(self.notificationShowMessage)
            oprot.writeFieldEnd()
        if self.notificationIncomingCall is not None:
            oprot.writeFieldBegin('notificationIncomingCall', TType.BOOL, 15)
            oprot.writeBool(self.notificationIncomingCall)
            oprot.writeFieldEnd()
        if self.notificationSoundMessage is not None:
            oprot.writeFieldBegin('notificationSoundMessage', TType.STRING, 16)
            oprot.writeString(self.notificationSoundMessage.encode('utf-8') if sys.version_info[0] == 2 else self.notificationSoundMessage)
            oprot.writeFieldEnd()
        if self.notificationSoundGroup is not None:
            oprot.writeFieldBegin('notificationSoundGroup', TType.STRING, 17)
            oprot.writeString(self.notificationSoundGroup.encode('utf-8') if sys.version_info[0] == 2 else self.notificationSoundGroup)
            oprot.writeFieldEnd()
        if self.notificationDisabledWithSub is not None:
            oprot.writeFieldBegin('notificationDisabledWithSub', TType.BOOL, 18)
            oprot.writeBool(self.notificationDisabledWithSub)
            oprot.writeFieldEnd()
        if self.privacySyncContacts is not None:
            oprot.writeFieldBegin('privacySyncContacts', TType.BOOL, 20)
            oprot.writeBool(self.privacySyncContacts)
            oprot.writeFieldEnd()
        if self.privacySearchByPhoneNumber is not None:
            oprot.writeFieldBegin('privacySearchByPhoneNumber', TType.BOOL, 21)
            oprot.writeBool(self.privacySearchByPhoneNumber)
            oprot.writeFieldEnd()
        if self.privacySearchByUserid is not None:
            oprot.writeFieldBegin('privacySearchByUserid', TType.BOOL, 22)
            oprot.writeBool(self.privacySearchByUserid)
            oprot.writeFieldEnd()
        if self.privacySearchByEmail is not None:
            oprot.writeFieldBegin('privacySearchByEmail', TType.BOOL, 23)
            oprot.writeBool(self.privacySearchByEmail)
            oprot.writeFieldEnd()
        if self.privacyAllowSecondaryDeviceLogin is not None:
            oprot.writeFieldBegin('privacyAllowSecondaryDeviceLogin', TType.BOOL, 24)
            oprot.writeBool(self.privacyAllowSecondaryDeviceLogin)
            oprot.writeFieldEnd()
        if self.privacyProfileImagePostToMyhome is not None:
            oprot.writeFieldBegin('privacyProfileImagePostToMyhome', TType.BOOL, 25)
            oprot.writeBool(self.privacyProfileImagePostToMyhome)
            oprot.writeFieldEnd()
        if self.privacyReceiveMessagesFromNotFriend is not None:
            oprot.writeFieldBegin('privacyReceiveMessagesFromNotFriend', TType.BOOL, 26)
            oprot.writeBool(self.privacyReceiveMessagesFromNotFriend)
            oprot.writeFieldEnd()
        if self.contactMyTicket is not None:
            oprot.writeFieldBegin('contactMyTicket', TType.STRING, 30)
            oprot.writeString(self.contactMyTicket.encode('utf-8') if sys.version_info[0] == 2 else self.contactMyTicket)
            oprot.writeFieldEnd()
        if self.identityProvider is not None:
            oprot.writeFieldBegin('identityProvider', TType.I32, 40)
            oprot.writeI32(self.identityProvider)
            oprot.writeFieldEnd()
        if self.identityIdentifier is not None:
            oprot.writeFieldBegin('identityIdentifier', TType.STRING, 41)
            oprot.writeString(self.identityIdentifier.encode('utf-8') if sys.version_info[0] == 2 else self.identityIdentifier)
            oprot.writeFieldEnd()
        if self.snsAccounts is not None:
            oprot.writeFieldBegin('snsAccounts', TType.MAP, 42)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.snsAccounts))
            for kiter268, viter269 in self.snsAccounts.items():
                oprot.writeI32(kiter268)
                oprot.writeString(viter269.encode('utf-8') if sys.version_info[0] == 2 else viter269)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.phoneRegistration is not None:
            oprot.writeFieldBegin('phoneRegistration', TType.BOOL, 43)
            oprot.writeBool(self.phoneRegistration)
            oprot.writeFieldEnd()
        if self.emailConfirmationStatus is not None:
            oprot.writeFieldBegin('emailConfirmationStatus', TType.I32, 44)
            oprot.writeI32(self.emailConfirmationStatus)
            oprot.writeFieldEnd()
        if self.preferenceLocale is not None:
            oprot.writeFieldBegin('preferenceLocale', TType.STRING, 50)
            oprot.writeString(self.preferenceLocale.encode('utf-8') if sys.version_info[0] == 2 else self.preferenceLocale)
            oprot.writeFieldEnd()
        if self.customModes is not None:
            oprot.writeFieldBegin('customModes', TType.MAP, 60)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.customModes))
            for kiter270, viter271 in self.customModes.items():
                oprot.writeI32(kiter270)
                oprot.writeString(viter271.encode('utf-8') if sys.version_info[0] == 2 else viter271)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SimpleChannelClient(object):
    """
    Attributes:
     - applicationType
     - applicationVersion
     - locale
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'applicationType', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'applicationVersion', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
    )

    def __init__(self, applicationType=None, applicationVersion=None, locale=None,):
        self.applicationType = applicationType
        self.applicationVersion = applicationVersion
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.applicationType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.applicationVersion = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SimpleChannelClient')
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.STRING, 1)
            oprot.writeString(self.applicationType.encode('utf-8') if sys.version_info[0] == 2 else self.applicationType)
            oprot.writeFieldEnd()
        if self.applicationVersion is not None:
            oprot.writeFieldBegin('applicationVersion', TType.STRING, 2)
            oprot.writeString(self.applicationVersion.encode('utf-8') if sys.version_info[0] == 2 else self.applicationVersion)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SimpleChannelContact(object):
    """
    Attributes:
     - mid
     - displayName
     - pictureStatus
     - picturePath
     - statusMessage
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'displayName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'pictureStatus', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'picturePath', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 5
    )

    def __init__(self, mid=None, displayName=None, pictureStatus=None, picturePath=None, statusMessage=None,):
        self.mid = mid
        self.displayName = displayName
        self.pictureStatus = pictureStatus
        self.picturePath = picturePath
        self.statusMessage = statusMessage

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.pictureStatus = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.picturePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SimpleChannelContact')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 2)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.pictureStatus is not None:
            oprot.writeFieldBegin('pictureStatus', TType.STRING, 3)
            oprot.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            oprot.writeFieldEnd()
        if self.picturePath is not None:
            oprot.writeFieldBegin('picturePath', TType.STRING, 4)
            oprot.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 5)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsFriend(object):
    """
    Attributes:
     - snsUserId
     - snsUserName
     - snsIdType
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'snsUserId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'snsUserName', 'UTF8', None, ),  # 2
        (3, TType.I32, 'snsIdType', None, None, ),  # 3
    )

    def __init__(self, snsUserId=None, snsUserName=None, snsIdType=None,):
        self.snsUserId = snsUserId
        self.snsUserName = snsUserName
        self.snsIdType = snsIdType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.snsUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.snsUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.snsIdType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsFriend')
        if self.snsUserId is not None:
            oprot.writeFieldBegin('snsUserId', TType.STRING, 1)
            oprot.writeString(self.snsUserId.encode('utf-8') if sys.version_info[0] == 2 else self.snsUserId)
            oprot.writeFieldEnd()
        if self.snsUserName is not None:
            oprot.writeFieldBegin('snsUserName', TType.STRING, 2)
            oprot.writeString(self.snsUserName.encode('utf-8') if sys.version_info[0] == 2 else self.snsUserName)
            oprot.writeFieldEnd()
        if self.snsIdType is not None:
            oprot.writeFieldBegin('snsIdType', TType.I32, 3)
            oprot.writeI32(self.snsIdType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsFriendContactRegistration(object):
    """
    Attributes:
     - contact
     - snsIdType
     - snsUserId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'contact', (Contact, Contact.thrift_spec), None, ),  # 1
        (2, TType.I32, 'snsIdType', None, None, ),  # 2
        (3, TType.STRING, 'snsUserId', 'UTF8', None, ),  # 3
    )

    def __init__(self, contact=None, snsIdType=None, snsUserId=None,):
        self.contact = contact
        self.snsIdType = snsIdType
        self.snsUserId = snsUserId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.contact = Contact()
                    self.contact.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.snsIdType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.snsUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsFriendContactRegistration')
        if self.contact is not None:
            oprot.writeFieldBegin('contact', TType.STRUCT, 1)
            self.contact.write(oprot)
            oprot.writeFieldEnd()
        if self.snsIdType is not None:
            oprot.writeFieldBegin('snsIdType', TType.I32, 2)
            oprot.writeI32(self.snsIdType)
            oprot.writeFieldEnd()
        if self.snsUserId is not None:
            oprot.writeFieldBegin('snsUserId', TType.STRING, 3)
            oprot.writeString(self.snsUserId.encode('utf-8') if sys.version_info[0] == 2 else self.snsUserId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsFriendModification(object):
    """
    Attributes:
     - type
     - snsFriend
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        (2, TType.STRUCT, 'snsFriend', (SnsFriend, SnsFriend.thrift_spec), None, ),  # 2
    )

    def __init__(self, type=None, snsFriend=None,):
        self.type = type
        self.snsFriend = snsFriend

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.snsFriend = SnsFriend()
                    self.snsFriend.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsFriendModification')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.snsFriend is not None:
            oprot.writeFieldBegin('snsFriend', TType.STRUCT, 2)
            self.snsFriend.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsFriends(object):
    """
    Attributes:
     - snsFriends
     - hasMore
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'snsFriends', (TType.STRUCT, (SnsFriend, SnsFriend.thrift_spec), False), None, ),  # 1
        (2, TType.BOOL, 'hasMore', None, None, ),  # 2
    )

    def __init__(self, snsFriends=None, hasMore=None,):
        self.snsFriends = snsFriends
        self.hasMore = hasMore

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.snsFriends = []
                    (_etype275, _size272) = iprot.readListBegin()
                    for _i276 in range(_size272):
                        _elem277 = SnsFriend()
                        _elem277.read(iprot)
                        self.snsFriends.append(_elem277)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.hasMore = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsFriends')
        if self.snsFriends is not None:
            oprot.writeFieldBegin('snsFriends', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.snsFriends))
            for iter278 in self.snsFriends:
                iter278.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.hasMore is not None:
            oprot.writeFieldBegin('hasMore', TType.BOOL, 2)
            oprot.writeBool(self.hasMore)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsIdUserStatus(object):
    """
    Attributes:
     - userExisting
     - phoneNumberRegistered
     - sameDevice
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'userExisting', None, None, ),  # 1
        (2, TType.BOOL, 'phoneNumberRegistered', None, None, ),  # 2
        (3, TType.BOOL, 'sameDevice', None, None, ),  # 3
    )

    def __init__(self, userExisting=None, phoneNumberRegistered=None, sameDevice=None,):
        self.userExisting = userExisting
        self.phoneNumberRegistered = phoneNumberRegistered
        self.sameDevice = sameDevice

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.userExisting = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.phoneNumberRegistered = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.sameDevice = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsIdUserStatus')
        if self.userExisting is not None:
            oprot.writeFieldBegin('userExisting', TType.BOOL, 1)
            oprot.writeBool(self.userExisting)
            oprot.writeFieldEnd()
        if self.phoneNumberRegistered is not None:
            oprot.writeFieldBegin('phoneNumberRegistered', TType.BOOL, 2)
            oprot.writeBool(self.phoneNumberRegistered)
            oprot.writeFieldEnd()
        if self.sameDevice is not None:
            oprot.writeFieldBegin('sameDevice', TType.BOOL, 3)
            oprot.writeBool(self.sameDevice)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SnsProfile(object):
    """
    Attributes:
     - snsUserId
     - snsUserName
     - email
     - thumbnailUrl
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'snsUserId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'snsUserName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'email', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'thumbnailUrl', 'UTF8', None, ),  # 4
    )

    def __init__(self, snsUserId=None, snsUserName=None, email=None, thumbnailUrl=None,):
        self.snsUserId = snsUserId
        self.snsUserName = snsUserName
        self.email = email
        self.thumbnailUrl = thumbnailUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.snsUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.snsUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.thumbnailUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SnsProfile')
        if self.snsUserId is not None:
            oprot.writeFieldBegin('snsUserId', TType.STRING, 1)
            oprot.writeString(self.snsUserId.encode('utf-8') if sys.version_info[0] == 2 else self.snsUserId)
            oprot.writeFieldEnd()
        if self.snsUserName is not None:
            oprot.writeFieldBegin('snsUserName', TType.STRING, 2)
            oprot.writeString(self.snsUserName.encode('utf-8') if sys.version_info[0] == 2 else self.snsUserName)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 3)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.thumbnailUrl is not None:
            oprot.writeFieldBegin('thumbnailUrl', TType.STRING, 4)
            oprot.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SystemConfiguration(object):
    """
    Attributes:
     - endpoint
     - endpointSsl
     - updateUrl
     - c2dmAccount
     - nniServer
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'endpoint', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'endpointSsl', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'updateUrl', 'UTF8', None, ),  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.STRING, 'c2dmAccount', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'nniServer', 'UTF8', None, ),  # 12
    )

    def __init__(self, endpoint=None, endpointSsl=None, updateUrl=None, c2dmAccount=None, nniServer=None,):
        self.endpoint = endpoint
        self.endpointSsl = endpointSsl
        self.updateUrl = updateUrl
        self.c2dmAccount = c2dmAccount
        self.nniServer = nniServer

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.endpoint = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.endpointSsl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.updateUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.c2dmAccount = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.nniServer = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SystemConfiguration')
        if self.endpoint is not None:
            oprot.writeFieldBegin('endpoint', TType.STRING, 1)
            oprot.writeString(self.endpoint.encode('utf-8') if sys.version_info[0] == 2 else self.endpoint)
            oprot.writeFieldEnd()
        if self.endpointSsl is not None:
            oprot.writeFieldBegin('endpointSsl', TType.STRING, 2)
            oprot.writeString(self.endpointSsl.encode('utf-8') if sys.version_info[0] == 2 else self.endpointSsl)
            oprot.writeFieldEnd()
        if self.updateUrl is not None:
            oprot.writeFieldBegin('updateUrl', TType.STRING, 3)
            oprot.writeString(self.updateUrl.encode('utf-8') if sys.version_info[0] == 2 else self.updateUrl)
            oprot.writeFieldEnd()
        if self.c2dmAccount is not None:
            oprot.writeFieldBegin('c2dmAccount', TType.STRING, 11)
            oprot.writeString(self.c2dmAccount.encode('utf-8') if sys.version_info[0] == 2 else self.c2dmAccount)
            oprot.writeFieldEnd()
        if self.nniServer is not None:
            oprot.writeFieldBegin('nniServer', TType.STRING, 12)
            oprot.writeString(self.nniServer.encode('utf-8') if sys.version_info[0] == 2 else self.nniServer)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TalkException(TException):
    """
    Attributes:
     - code
     - reason
     - parameterMap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None, ),  # 1
        (2, TType.STRING, 'reason', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'parameterMap', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, code=None, reason=None, parameterMap=None,):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype280, _vtype281, _size279) = iprot.readMapBegin()
                    for _i283 in range(_size279):
                        _key284 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val285 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key284] = _val285
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TalkException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 2)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter286, viter287 in self.parameterMap.items():
                oprot.writeString(kiter286.encode('utf-8') if sys.version_info[0] == 2 else kiter286)
                oprot.writeString(viter287.encode('utf-8') if sys.version_info[0] == 2 else viter287)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Ticket(object):
    """
    Attributes:
     - id
     - expirationTime
     - maxUseCount
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        None,  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.I64, 'expirationTime', None, None, ),  # 10
        None,  # 11
        None,  # 12
        None,  # 13
        None,  # 14
        None,  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        (21, TType.I32, 'maxUseCount', None, None, ),  # 21
    )

    def __init__(self, id=None, expirationTime=None, maxUseCount=None,):
        self.id = id
        self.expirationTime = expirationTime
        self.maxUseCount = maxUseCount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.expirationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.maxUseCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Ticket')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.expirationTime is not None:
            oprot.writeFieldBegin('expirationTime', TType.I64, 10)
            oprot.writeI64(self.expirationTime)
            oprot.writeFieldEnd()
        if self.maxUseCount is not None:
            oprot.writeFieldBegin('maxUseCount', TType.I32, 21)
            oprot.writeI32(self.maxUseCount)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TMessageBox(object):
    """
    Attributes:
     - id
     - channelId
     - lastSeq
     - unreadCount
     - lastModifiedTime
     - status
     - midType
     - lastMessages
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'channelId', 'UTF8', None, ),  # 2
        None,  # 3
        None,  # 4
        (5, TType.I64, 'lastSeq', None, None, ),  # 5
        (6, TType.I64, 'unreadCount', None, None, ),  # 6
        (7, TType.I64, 'lastModifiedTime', None, None, ),  # 7
        (8, TType.I32, 'status', None, None, ),  # 8
        (9, TType.I32, 'midType', None, None, ),  # 9
        (10, TType.LIST, 'lastMessages', (TType.STRUCT, (Message, Message.thrift_spec), False), None, ),  # 10
    )

    def __init__(self, id=None, channelId=None, lastSeq=None, unreadCount=None, lastModifiedTime=None, status=None, midType=None, lastMessages=None,):
        self.id = id
        self.channelId = channelId
        self.lastSeq = lastSeq
        self.unreadCount = unreadCount
        self.lastModifiedTime = lastModifiedTime
        self.status = status
        self.midType = midType
        self.lastMessages = lastMessages

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.lastSeq = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.unreadCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.lastModifiedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.midType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.lastMessages = []
                    (_etype291, _size288) = iprot.readListBegin()
                    for _i292 in range(_size288):
                        _elem293 = Message()
                        _elem293.read(iprot)
                        self.lastMessages.append(_elem293)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TMessageBox')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 2)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.lastSeq is not None:
            oprot.writeFieldBegin('lastSeq', TType.I64, 5)
            oprot.writeI64(self.lastSeq)
            oprot.writeFieldEnd()
        if self.unreadCount is not None:
            oprot.writeFieldBegin('unreadCount', TType.I64, 6)
            oprot.writeI64(self.unreadCount)
            oprot.writeFieldEnd()
        if self.lastModifiedTime is not None:
            oprot.writeFieldBegin('lastModifiedTime', TType.I64, 7)
            oprot.writeI64(self.lastModifiedTime)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 8)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.midType is not None:
            oprot.writeFieldBegin('midType', TType.I32, 9)
            oprot.writeI32(self.midType)
            oprot.writeFieldEnd()
        if self.lastMessages is not None:
            oprot.writeFieldBegin('lastMessages', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.lastMessages))
            for iter294 in self.lastMessages:
                iter294.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TMessageBoxWrapUp(object):
    """
    Attributes:
     - messageBox
     - name
     - contacts
     - pictureRevision
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'messageBox', (TMessageBox, TMessageBox.thrift_spec), None, ),  # 1
        (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
        (3, TType.LIST, 'contacts', (TType.STRUCT, (Contact, Contact.thrift_spec), False), None, ),  # 3
        (4, TType.STRING, 'pictureRevision', 'UTF8', None, ),  # 4
    )

    def __init__(self, messageBox=None, name=None, contacts=None, pictureRevision=None,):
        self.messageBox = messageBox
        self.name = name
        self.contacts = contacts
        self.pictureRevision = pictureRevision

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.messageBox = TMessageBox()
                    self.messageBox.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.contacts = []
                    (_etype298, _size295) = iprot.readListBegin()
                    for _i299 in range(_size295):
                        _elem300 = Contact()
                        _elem300.read(iprot)
                        self.contacts.append(_elem300)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pictureRevision = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TMessageBoxWrapUp')
        if self.messageBox is not None:
            oprot.writeFieldBegin('messageBox', TType.STRUCT, 1)
            self.messageBox.write(oprot)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.contacts is not None:
            oprot.writeFieldBegin('contacts', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.contacts))
            for iter301 in self.contacts:
                iter301.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.pictureRevision is not None:
            oprot.writeFieldBegin('pictureRevision', TType.STRING, 4)
            oprot.writeString(self.pictureRevision.encode('utf-8') if sys.version_info[0] == 2 else self.pictureRevision)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TMessageBoxWrapUpResponse(object):
    """
    Attributes:
     - messageBoxWrapUpList
     - totalSize
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'messageBoxWrapUpList', (TType.STRUCT, (TMessageBoxWrapUp, TMessageBoxWrapUp.thrift_spec), False), None, ),  # 1
        (2, TType.I32, 'totalSize', None, None, ),  # 2
    )

    def __init__(self, messageBoxWrapUpList=None, totalSize=None,):
        self.messageBoxWrapUpList = messageBoxWrapUpList
        self.totalSize = totalSize

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.messageBoxWrapUpList = []
                    (_etype305, _size302) = iprot.readListBegin()
                    for _i306 in range(_size302):
                        _elem307 = TMessageBoxWrapUp()
                        _elem307.read(iprot)
                        self.messageBoxWrapUpList.append(_elem307)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.totalSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TMessageBoxWrapUpResponse')
        if self.messageBoxWrapUpList is not None:
            oprot.writeFieldBegin('messageBoxWrapUpList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.messageBoxWrapUpList))
            for iter308 in self.messageBoxWrapUpList:
                iter308.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.totalSize is not None:
            oprot.writeFieldBegin('totalSize', TType.I32, 2)
            oprot.writeI32(self.totalSize)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UniversalNotificationServiceException(TException):
    """
    Attributes:
     - code
     - reason
     - parameterMap
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None, ),  # 1
        (2, TType.STRING, 'reason', 'UTF8', None, ),  # 2
        (3, TType.MAP, 'parameterMap', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, code=None, reason=None, parameterMap=None,):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.reason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.parameterMap = {}
                    (_ktype310, _vtype311, _size309) = iprot.readMapBegin()
                    for _i313 in range(_size309):
                        _key314 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val315 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.parameterMap[_key314] = _val315
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('UniversalNotificationServiceException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.reason is not None:
            oprot.writeFieldBegin('reason', TType.STRING, 2)
            oprot.writeString(self.reason.encode('utf-8') if sys.version_info[0] == 2 else self.reason)
            oprot.writeFieldEnd()
        if self.parameterMap is not None:
            oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
            for kiter316, viter317 in self.parameterMap.items():
                oprot.writeString(kiter316.encode('utf-8') if sys.version_info[0] == 2 else kiter316)
                oprot.writeString(viter317.encode('utf-8') if sys.version_info[0] == 2 else viter317)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UpdateBuddyProfileResult(object):
    """
    Attributes:
     - requestId
     - state
     - eventNo
     - receiverCount
     - successCount
     - failCount
     - cancelCount
     - unregisterCount
     - timestamp
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'state', None, None, ),  # 2
        (3, TType.I32, 'eventNo', None, None, ),  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        None,  # 10
        (11, TType.I64, 'receiverCount', None, None, ),  # 11
        (12, TType.I64, 'successCount', None, None, ),  # 12
        (13, TType.I64, 'failCount', None, None, ),  # 13
        (14, TType.I64, 'cancelCount', None, None, ),  # 14
        (15, TType.I64, 'unregisterCount', None, None, ),  # 15
        None,  # 16
        None,  # 17
        None,  # 18
        None,  # 19
        None,  # 20
        (21, TType.I64, 'timestamp', None, None, ),  # 21
        (22, TType.STRING, 'message', 'UTF8', None, ),  # 22
    )

    def __init__(self, requestId=None, state=None, eventNo=None, receiverCount=None, successCount=None, failCount=None, cancelCount=None, unregisterCount=None, timestamp=None, message=None,):
        self.requestId = requestId
        self.state = state
        self.eventNo = eventNo
        self.receiverCount = receiverCount
        self.successCount = successCount
        self.failCount = failCount
        self.cancelCount = cancelCount
        self.unregisterCount = unregisterCount
        self.timestamp = timestamp
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eventNo = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.receiverCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.successCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.failCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.cancelCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I64:
                    self.unregisterCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('UpdateBuddyProfileResult')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.state is not None:
            oprot.writeFieldBegin('state', TType.I32, 2)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.eventNo is not None:
            oprot.writeFieldBegin('eventNo', TType.I32, 3)
            oprot.writeI32(self.eventNo)
            oprot.writeFieldEnd()
        if self.receiverCount is not None:
            oprot.writeFieldBegin('receiverCount', TType.I64, 11)
            oprot.writeI64(self.receiverCount)
            oprot.writeFieldEnd()
        if self.successCount is not None:
            oprot.writeFieldBegin('successCount', TType.I64, 12)
            oprot.writeI64(self.successCount)
            oprot.writeFieldEnd()
        if self.failCount is not None:
            oprot.writeFieldBegin('failCount', TType.I64, 13)
            oprot.writeI64(self.failCount)
            oprot.writeFieldEnd()
        if self.cancelCount is not None:
            oprot.writeFieldBegin('cancelCount', TType.I64, 14)
            oprot.writeI64(self.cancelCount)
            oprot.writeFieldEnd()
        if self.unregisterCount is not None:
            oprot.writeFieldBegin('unregisterCount', TType.I64, 15)
            oprot.writeI64(self.unregisterCount)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 21)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 22)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UserAuthStatus(object):
    """
    Attributes:
     - phoneNumberRegistered
     - registeredSnsIdTypes
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'phoneNumberRegistered', None, None, ),  # 1
        (2, TType.LIST, 'registeredSnsIdTypes', (TType.I32, None, False), None, ),  # 2
    )

    def __init__(self, phoneNumberRegistered=None, registeredSnsIdTypes=None,):
        self.phoneNumberRegistered = phoneNumberRegistered
        self.registeredSnsIdTypes = registeredSnsIdTypes

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.phoneNumberRegistered = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.registeredSnsIdTypes = []
                    (_etype321, _size318) = iprot.readListBegin()
                    for _i322 in range(_size318):
                        _elem323 = iprot.readI32()
                        self.registeredSnsIdTypes.append(_elem323)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('UserAuthStatus')
        if self.phoneNumberRegistered is not None:
            oprot.writeFieldBegin('phoneNumberRegistered', TType.BOOL, 1)
            oprot.writeBool(self.phoneNumberRegistered)
            oprot.writeFieldEnd()
        if self.registeredSnsIdTypes is not None:
            oprot.writeFieldBegin('registeredSnsIdTypes', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.registeredSnsIdTypes))
            for iter324 in self.registeredSnsIdTypes:
                oprot.writeI32(iter324)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class WapInvitation(object):
    """
    Attributes:
     - type
     - inviteeEmail
     - inviterMid
     - roomMid
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        None,  # 2
        None,  # 3
        None,  # 4
        None,  # 5
        None,  # 6
        None,  # 7
        None,  # 8
        None,  # 9
        (10, TType.STRING, 'inviteeEmail', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'inviterMid', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'roomMid', 'UTF8', None, ),  # 12
    )

    def __init__(self, type=None, inviteeEmail=None, inviterMid=None, roomMid=None,):
        self.type = type
        self.inviteeEmail = inviteeEmail
        self.inviterMid = inviterMid
        self.roomMid = roomMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.inviteeEmail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.inviterMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.roomMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('WapInvitation')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.inviteeEmail is not None:
            oprot.writeFieldBegin('inviteeEmail', TType.STRING, 10)
            oprot.writeString(self.inviteeEmail.encode('utf-8') if sys.version_info[0] == 2 else self.inviteeEmail)
            oprot.writeFieldEnd()
        if self.inviterMid is not None:
            oprot.writeFieldBegin('inviterMid', TType.STRING, 11)
            oprot.writeString(self.inviterMid.encode('utf-8') if sys.version_info[0] == 2 else self.inviterMid)
            oprot.writeFieldEnd()
        if self.roomMid is not None:
            oprot.writeFieldBegin('roomMid', TType.STRING, 12)
            oprot.writeString(self.roomMid.encode('utf-8') if sys.version_info[0] == 2 else self.roomMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
