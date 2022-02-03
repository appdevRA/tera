from django.db import models
from django.utils import timezone
from django.db.models import Q


class BookmarkQuerySet(models.QuerySet):
    def recently_added(self):
        seven_days_ago = timezone.now() - timezone.timedelta(days=7)
        return self.filter(dateAdded__gte=seven_days_ago)

    def recently_read(self):
        three_days_ago = timezone.now() - timezone.timedelta(days=3)
        return self.filter(dateAccessed__gte=three_days_ago)

    def favorites(self, favorite=True):
        return self.filter(isFavorite=favorite)

    def unarchived(self):
        return self.filter(isRemoved=0)

    def archived(self):
        return self.filter(isRemoved=1)

    def removed(self):
        return self.filter(isRemoved=2)

    def user(self, user):
        return self.filter(user=user)

    def bookmark(self, bookmark):
        return self.filter(bookmark=bookmark)

    def groups_only(self, groups_only):
        return self.filter(group__isnull=not groups_only)

    def group(self, group):
        return self.filter(group=group)

    def folder(self, folder):
        return self.filter(folders=folder)


class GroupQuerySet(models.QuerySet):
    def for_user(self, user_id: int):
        owner_filter = Q(owner_id=user_id)
        member_filter = Q(member__id=user_id)

        return self.filter(owner_filter).union(self.filter(member_filter))

    def available_for_bookmark_detail(self, bookmark_detail_id: int):
        return self.exclude(bookmark__bookmark_id=bookmark_detail_id).union(
            self.filter(
                ~Q(bookmark__isRemoved=0)
                & Q(bookmark__bookmark_id=bookmark_detail_id)
            )
        )