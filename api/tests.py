import json

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase


class MyFancyTestCase(GraphQLTestCase):
    def test_most_popular_books_query(self):
        response = self.query(
            '''
                    query {
                mostPopular {
                    title
                }
                }

            ''',
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)

    def test_get_books_by_user(self):
        response = self.query(
            '''
                query {
                booksByUser(ownedBy: 1) {
                    title
                } 

                }
            ''',
        )

        content = json.loads(response.content)


        self.assertResponseNoErrors(response)

    def test_search_books(self):
        response = self.query(
            '''
            query {
            searchBooks(query: "test" ) {
                title
            } 

            }
            ''',
        )

        content = json.loads(response.content)


        self.assertResponseNoErrors(response)

    
