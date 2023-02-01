from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):
    # Отзывы на странице фильма
    model = Reviews
    extra = 1  # одно пустое поле
    readonly_fields = ('name', 'email')

class MovieShotsInline(admin.TabularInline):
    # кадры из фильма на странице фильма
    model = MovieShots
    extra = 1
    '''вывод изображений '''
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInLine]
    save_on_top = True  # меню сохранения вверх
    save_as = True  # изменение кнопок меню
    list_editable = ('draft',)
    readonly_fields = ("get_image",)
    '''групировка полей'''
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
             "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),  # свернутое поле
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    '''вывод картинки постера'''
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"


# admin.site.register(Reviews)
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


# admin.site.register(Genre)
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


# admin.site.register(MovieShots)
@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie" , "get_image")
    '''вывод изображений '''
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60" ')

    get_image.short_description = 'Изображение'


# admin.site.register(Actor)
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", 'get_image')
    '''вывод изображений '''
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60" ')

    get_image.short_description = 'Изображение'


admin.site.register(Rating)
admin.site.register(RatingStar)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
