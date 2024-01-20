### How to run
1) Clone repository
    ```
    git clone https://github.com/mykolamateichuk/autotest_ajax_app_using_appium.git
    ```
2) Go into the created folder

    ```
    cd autotest_ajax_app_using_appium
    ```

3) Create and launch virtual environment
    
    Windows
    ```
    python -m venv venv
    ```
   
    ```
    .\venv\Scripts\activate
    ```
   
    MacOS
    ```
    python3 -m venv venv
    ```
   
    ```
    source venv/bin/activate
    ```

4) Install requirements

   ```
   pip install -r requirements.txt
   ```

5) Set needed environment variables
   
   Windows
   ```
   set ANDROID_HOME=path\to\your\android\sdk
   ```
   
   MacOS
   ```
   export $ANDROID_HOME=path/to/your/android/sdk
   ```

6) Run appium server

   ```
   appium -a 0.0.0.0 -p 4723 --allow-insecure adb_shell
   ```

7) Open new terminal in the same folder and run

   ```
   pytest -s
   ```
### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).
3) Использовать параметризацию.
4) Закомитить выполненное задание на гитхаб.

### Дополнительное задание (опционально)
1) *Реализовать логирование теста.
2) *Реализовать динамическое определение udid телефона через subprocess
3) **Написать на проверку элементов SideBar (выезжающее меню слева).

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - https://appium.io/docs/en/2.0/quickstart/
5) Инспектор приложения - https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/

### Login credentials
login - qa.ajax.app.automation@gmail.com
password - qa_automation_password
