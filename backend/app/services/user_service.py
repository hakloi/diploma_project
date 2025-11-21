from datetime import datetime

# Test users database
users = {
    1: {
        "user_id": 1,
        "username": "alice",
        "email": "alice@example.com",
        "password_hash": "123",
        "created_at": datetime(2024, 1, 15, 10, 30, 0),
        "last_login": datetime(2024, 1, 20, 14, 22, 0),
        "is_active": True,
        "is_online": False,
        "skill_level": "beginner",
        "preferred_topics": "math,python",
        "learning_goals": "Learn ML basics",
        "completed_topics": "python_basics",
        "total_progress": 25,
        "current_topic_id": 2,
        "streak_days": 5
    },
    2: {
        "user_id": 2,
        "username": "bob",
        "email": "bob@example.com",
        "password_hash": "456",
        "created_at": datetime(2024, 1, 10, 9, 15, 0),
        "last_login": datetime(2024, 1, 21, 16, 45, 0),
        "is_active": True,
        "is_online": True,
        "skill_level": "intermediate",
        "preferred_topics": "ml,ai,cv",
        "learning_goals": "Master computer vision",
        "completed_topics": "python_basics,ml_intro",
        "total_progress": 60,
        "current_topic_id": 5,
        "streak_days": 12
    },
    3: {
        "user_id": 3,
        "username": "alex",
        "email": "alex@example.com",
        "password_hash": "789",
        "created_at": datetime(2024, 1, 5, 8, 0, 0),
        "last_login": datetime(2024, 1, 19, 12, 30, 0),
        "is_active": True,
        "is_online": False,
        "skill_level": "advanced",
        "preferred_topics": "ai,nlp,alg",
        "learning_goals": "Research in NLP",
        "completed_topics": "python_basics,ml_intro,deep_learning",
        "total_progress": 85,
        "current_topic_id": 8,
        "streak_days": 30
    }
}
