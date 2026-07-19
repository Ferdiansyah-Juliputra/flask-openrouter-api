from io import BytesIO

def test_review_success(client, monkeypatch):
    monkeypatch.setattr(
        "app.routes.review.review_resume",
        lambda resume, requirement: "ATS Score: 85"
    )

    monkeypatch.setattr(
        "app.routes.review.load_document",
        lambda path: "Python Flask Docker"
    )

    data = {
        "resume": (
            BytesIO(b"dummy pdf"),
            "resume.pdf"
        ),
        "requirement": "Looking for Python Developer"
    }

    response = client.post(
        "/review",
        data=data,
        content_type="multipart/form-data"
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["success"] is True

from io import BytesIO


def test_review_without_requirement(client):
    response = client.post(
        "/review",
        data={
            "resume": (
                BytesIO(b"dummy"),
                "resume.pdf"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 400

    body = response.get_json()

    assert body["success"] is False

from io import BytesIO


def test_review_without_requirement(client):
    response = client.post(
        "/review",
        data={
            "resume": (
                BytesIO(b"dummy"),
                "resume.pdf"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 400

    body = response.get_json()

    assert body["success"] is False