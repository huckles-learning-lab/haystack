from haystack.database.base import Document
import pytest


@pytest.mark.parametrize("document_store_with_docs", [("elasticsearch")], indirect=True)
def test_dummy_retriever(document_store_with_docs):
    from haystack.retriever.sparse import ElasticsearchFilterOnlyRetriever
    retriever = ElasticsearchFilterOnlyRetriever(document_store_with_docs)

    result = retriever.retrieve(query="godzilla", filters={"name": ["filename1"]}, top_k=1)
    assert type(result[0]) == Document
    assert result[0].text == "My name is Carla and I live in Berlin"
    assert result[0].meta["name"] == "filename1"

    result = retriever.retrieve(query="godzilla", filters={"name": ["filename1"]}, top_k=5)
    assert type(result[0]) == Document
    assert result[0].text == "My name is Carla and I live in Berlin"
    assert result[0].meta["name"] == "filename1"

    result = retriever.retrieve(query="godzilla", filters={"name": ["filename3"]}, top_k=5)
    assert type(result[0]) == Document
    assert result[0].text == "My name is Christelle and I live in Paris"
    assert result[0].meta["name"] == "filename3"

