# backend_test_case

Треба спроєктувати та написати відмовостійкий та масштабований REST-сервіс 
для зберігання бінарних даних в будь-якому хмарному сервісі (S3, Azure Blob Storage, Dropbox і тд). 
Доступ до даних здійснюється по ключу (key-value).

Вимоги до сервісу:
  - Операції put, get через REST
  - Синхронний запис (дані доступні через get одразу після завершення put)
  - Можна використовувати будь-який фреймворк, окрім Django
