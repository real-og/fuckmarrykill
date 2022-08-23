class Person:
    def __init__(self, name, picture = None) -> None:
        self.name = name
        self.picture = picture

defaultChars = [Person('Альберт Эйнштейн (Молодой)', 'https://i1.sndcdn.com/avatars-000511050333-lwzx4f-t240x240.jpg'),
                Person('Дора', 'https://www.vokrug.tv/pic/person/9/6/b/e/96be4387087c86e3e741e5797be4a415.jpg'),
                Person('Кендрик Ламар', 'https://www.rap.ru/upload/img/6466.jpg'),
                Person('Эвелина Хромченко', 'https://www.globalmsk.ru/usr/upload/upload-16290376990.jpg'),
                Person('Магнус Карлсен', 'https://en.chessbase.com/portals/all/2020/08/norway-chess-preview/Carlsen-Norway.jpg'),
                Person('Лара Крофт', 'https://st.overclockers.ru/legacy/blog/293072/105894_O.png'),
]