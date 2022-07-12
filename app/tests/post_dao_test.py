from app.post.dao.post_dao import PostDAO, DATA_PATH

import pytest

# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def post_dao():
    post_dao_instance = PostDAO(DATA_PATH)
    return post_dao_instance

# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"poster_name", "poster_avatar", "pic", "content ", "views_count","likes_count","pk"}

class TestPostDao:

    def test_get_all(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_post_by_pk(self, post_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        post = post_dao.get_post_by_pk(1)
        assert(post["pk"] == 1), "возвращается неправильный пост"
        assert set(post.keys()) == keys_should_be, "неверный список ключей"