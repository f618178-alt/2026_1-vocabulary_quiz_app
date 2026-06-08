from __future__ import annotations

from vocabulary_quiz_app.quiz_logic import Word

WORDS: list[Word] = [
    Word(term="apple", meaning="사과", difficulty="easy"),
    Word(term="book", meaning="책", difficulty="easy"),
    Word(term="chair", meaning="의자", difficulty="easy"),
    Word(term="door", meaning="문", difficulty="medium"),
    Word(term="flower", meaning="꽃", difficulty="medium"),
    Word(term="friend", meaning="친구", difficulty="medium"),
    Word(term="music", meaning="음악", difficulty="medium"),
    Word(term="school", meaning="학교", difficulty="hard"),
    Word(term="summer", meaning="여름", difficulty="hard"),
    Word(term="water", meaning="물", difficulty="hard"),
]
