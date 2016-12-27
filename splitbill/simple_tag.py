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
                tag, _ = Tag.objects.get_or_create(name="both")
                transaction.tags.add(tag)
                tag, _ = Tag.objects.get_or_create(name="shopping")
            transaction.tags.add(tag)
        if "sainsburys" in simple_check or "tesco" in simple_check or "poundland" in simple_check or "iceland" in simple_check:
            tag, _ = Tag.objects.get_or_create(name="both")
            transaction.tags.add(tag)
            tag, _ = Tag.objects.get_or_create(name="shopping")
            transaction.tags.add(tag)
        if "lul" in simple_check or "tsgn" in simple_check:
            tag, _ = Tag.objects.get_or_create(name="marco")
            transaction.tags.add(tag)
            tag, _ = Tag.objects.get_or_create(name="travel")
            transaction.tags.add(tag)
