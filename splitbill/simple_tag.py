from models import Tag

class SimpleTag:
    def tag(self, transaction):
        simple_check = transaction.description.lower()
        if "morrison" in simple_check:
            if "welwyn" in simple_check:
                tag, _ = Tag.objects.get_or_create(name="marco")
                transaction.tags.add(tag)
                tag, _ = Tag.objects.get_or_create(name="lunch")
            else:
                tag, _ = Tag.objects.get_or_create(name="shopping")
            transaction.tags.add(tag)
        if "tesco" in simple_check:
            tag, _ = Tag.objects.get_or_create(name="shopping")
            transaction.tags.add(tag)
