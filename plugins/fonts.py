

class Fonts:
    def typewriter(text):
        style = {
            'د': '𒄑',
            'ج': '𒌑',
            'ح': '𒃻',
            'خ': '𒋛',
            'ه': '𒈠',
            'ع': '𒌆',
            'غ': '𒉺',
            'ف': '𒅖',
            'ق': '𒄩',
            'ث': '𒐉',
            'ص': '𒊑',
            'ض': '𒈠',
            'ط': '𒅆',
            'ك': '𒈠',
            'م': '𒀭',
            'ن': ' 𒌑',
            'ت': '𒌓',
            'ا': '𒐕',
            'ل': '𒈨',
            'ب': '𒋙',
            'ي': '𒃻',
            'س': '𒂍',
            'ش': '𒌋',
            'ظ': '𒊬',
            'ز': '𒂟',
            'ة': '𒌓',
            'ى': '𒍮',
            'لا': '𒌦',
            'ر': '𒅆',
            'و': '𒊩',
            'ء': '𒅆',
            'ئ': '𒍮',
            'أ': '𒋙',
            'إ': '𒋙'

        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text