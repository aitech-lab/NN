Настройка окружения
-------------------

* http://deeplearning.net/software/theano/library/config.html

Работоспособность проверена с python 3.5.2

Питон должен быть собран с ключом `--enable-shared`

```
configrue --enable-shared
make
sudo make install
```

В папке `sentiments/python` создается виртуальное окружение

```
virtualenv -p /usr/local/bin/python3.5 env
source env/bin/activate
```

В окружение ставятся numpy keras theano h5py


```
pip install numpy theano keras h5py
```

Возможно понадобится указать путь к shared библиотекам питона (луше прописать это куда-нибудь в профиль)

`export LD_LIBRARY_PATH=/usr/local/lib`

Редактируем конфиг `~/.theanorc`, включаем GPU

```
[global]
floatX = float32
device = gpu0

[lib]
cnmem = 1
```

Запускает обучение:

`./train.py train-corpus.tsv test-corpus.tsv`

Проверка нагрузки на gpu `nvidia-smi`



python
------

encode-pipe.py
normalize-stat.py
slang.py
smile.py
stat-fast.py
stat-norm.py
stat-slow.py
stemmer.py
train.py
vocabulary.py

node
----

mystem.iced
slang.iced
stat.iced
