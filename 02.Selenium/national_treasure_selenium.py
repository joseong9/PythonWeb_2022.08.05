{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "HY92BNM3EI69"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "The system cannot find the path specified.\n",
            "The system cannot find the path specified.\n",
            "The system cannot find the path specified.\n"
          ]
        }
      ],
      "source": [
        "!apt-get update > /dev/null 2>&1\n",
        "!pip install selenium > /dev/null 2>&1\n",
        "!apt install chromium-chromedriver > /dev/null 2>&1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "zhtsQbvKIn3s"
      },
      "outputs": [
        {
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'selenium'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[1;32mc:\\Workspace\\01.PythonWeb\\02.Selenium\\national_treasure_selenium.ipynb 셀 2\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W1sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mtime\u001b[39;00m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W1sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mselenium\u001b[39;00m \u001b[39mimport\u001b[39;00m webdriver\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W1sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mselenium\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mwebdriver\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mcommon\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mkeys\u001b[39;00m \u001b[39mimport\u001b[39;00m Keys\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W1sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mselenium\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mwebdriver\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mcommon\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mby\u001b[39;00m \u001b[39mimport\u001b[39;00m By\n",
            "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'selenium'"
          ]
        }
      ],
      "source": [
        "import time\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.common.keys import Keys\n",
        "from selenium.webdriver.common.by import By\n",
        "from bs4 import BeautifulSoup\n",
        "import requests"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 129,
      "metadata": {
        "id": "91lG_BdeFCAh"
      },
      "outputs": [],
      "source": [
        "options = webdriver.ChromeOptions()\n",
        "# options.add_argument('--headless')   # 화면없이 실행\n",
        "# options.add_argument('--no-sandbox')\n",
        "# options.add_argument(\"--single-process\")\n",
        "# options.add_argument(\"--disable-dev-shm-usage\")\n",
        "driver = webdriver.Chrome('chromedriver', options=options)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 130,
      "metadata": {
        "id": "_tnPDmeaJQhA"
      },
      "outputs": [],
      "source": [
        "url = 'https://www.google.co.kr/'\n",
        "driver.get(url)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 131,
      "metadata": {
        "id": "_5iqAE0dLF7M"
      },
      "outputs": [],
      "source": [
        "#구글 검색 상단에 숭례문 검색\n",
        "search_box = driver.find_element(by=By.NAME, value='q')\n",
        "search_box.send_keys('숭례문')\n",
        "search_box.send_keys(Keys.ENTER)\n",
        "time.sleep(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 132,
      "metadata": {},
      "outputs": [],
      "source": [
        "driver.find_element_by_xpath('//*[@id=\"hdtb-msb\"]/div[1]/div/div[2]/a').click() #이미지 클릭\n",
        "time.sleep(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 134,
      "metadata": {},
      "outputs": [],
      "source": [
        "driver.find_element_by_class_name('rg_i').click()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 135,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[]"
            ]
          },
          "execution_count": 135,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "images = driver.find_elements_by_class_name('rg_i')\n",
        "count = 1\n",
        "for image in images:\n",
        "    driver.find_element_by_xpath('//*[@id=\"islrg\"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')\n",
        "    count +=1\n",
        "    if count == 2:\n",
        "        break"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 115,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "Nw_QKEfdOtCG",
        "outputId": "91cf02fc-2a52-4e00-a7da-052c1c74e4d5"
      },
      "outputs": [
        {
          "ename": "IndexError",
          "evalue": "list index out of range",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[1;32mc:\\Workspace\\01.PythonWeb\\02.Selenium\\national_treasure_selenium.ipynb 셀 8\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W6sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m div \u001b[39m=\u001b[39m divs[\u001b[39m0\u001b[39;49m]\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W6sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m title \u001b[39m=\u001b[39m div\u001b[39m.\u001b[39mfind_element(By\u001b[39m.\u001b[39mCSS_SELECTOR, \u001b[39m'\u001b[39m\u001b[39m.LC20lb.MBeuO.DKV0Md\u001b[39m\u001b[39m'\u001b[39m)\u001b[39m.\u001b[39mtext\u001b[39m.\u001b[39mstrip()\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Workspace/01.PythonWeb/02.Selenium/national_treasure_selenium.ipynb#W6sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m title\n",
            "\u001b[1;31mIndexError\u001b[0m: list index out of range"
          ]
        }
      ],
      "source": [
        "\n",
        "div = divs[0]\n",
        "title = div.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md').text.strip()\n",
        "title"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 55
        },
        "id": "pm_OXCkiQeaP",
        "outputId": "b1001801-c66d-43a9-baea-a629e8108719"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'ChromeDriver 105.0.5195.19 · Supports Chrome version 10 · For more details, please see the · ChromeDriver 104.0.5112.79 · Supports Chrome version 104 · For more ...'"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "content = div.find_element(By.CSS_SELECTOR, '.VwiC3b.yXK7lf.MUxGbd.yDYNvb').text.strip()\n",
        "content"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j1LZBNmxRwa4",
        "outputId": "b19844bb-90fe-430e-9bf2-990c281461ea"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[['WebDriver for Chrome - Downloads',\n",
              "  'ChromeDriver 105.0.5195.19 · Supports Chrome version 10 · For more details, please see the · ChromeDriver 104.0.5112.79 · Supports Chrome version 104 · For more ...'],\n",
              " ['[Python] Selenium 사용법, ChromeDriver 설치 방법',\n",
              "  '2020. 2. 22. — 하단에 Install Package 버튼을 눌러줍니다! ChromeDriver 설치방법. 일단 Chrome이 있어야 되겠죠? Chrome을 설치해줍니다! Chrome Version 확인.'],\n",
              " ['selenium) 설치하기! chromedriver 버전 오류 해결하기 - 블로그',\n",
              "  '2019. 5. 17. — 여기에서 현재 사용중인 크롬의 버전과 일치하는 버전의 파일을 다운 받으시면 됩니다. 저 같은 경우는 버전 74에 해당하니 ChromeDriver ...'],\n",
              " ['Chromedriver 다운로드 및 설치하는 법 - 코딩으로 자아실현',\n",
              "  '2021. 9. 25. — 여기서는 Chrome의 Webdriver인 Chromedriver를 다운 받는 법을 알아봅니다. 크롬드라이버를 실행하면 위와 같이 소프트웨어에 의해 제어되고 있다는 ...'],\n",
              " ['104.0.5112.20 - Chrome driver',\n",
              "  'Name, Last modified, Size, ETag. [DIR], Parent Directory, -. [DIR], chromedriver_linux64.zip, 2022-06-24 08:23:08, 6.42MB, 8836e9b20a02e9a65826d29050b33b3c.'],\n",
              " ['3분 안에 해결하는 크롬 드라이버 버전 오류 - Unlimited',\n",
              "  '2022. 5. 18. — SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 99 Current browser ...'],\n",
              " ['chromedriver - npm',\n",
              "  '2022. 8. 3. — ChromeDriver for Selenium. Latest version: 104.0.0, last published: 15 days ago. Start using chromedriver in your project by running `npm i ...'],\n",
              " ['Install browser drivers - Selenium',\n",
              "  'ChromeDriver driver = new ChromeDriver(); ... Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping  ...'],\n",
              " ['Index of /chromedriver - CNPM Binaries Mirror',\n",
              "  'Index of /chromedriver/. [ICO], Name, Last modified, Size. [DIR], Parent Directory, -. [DIR], 100.0.4896.20/, 2022-08-16T09:00:00Z, -. [DIR] ...']]"
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "lines = []\n",
        "for div in divs:\n",
        "    try:\n",
        "        title = div.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md').text\n",
        "        content = div.find_element(By.CSS_SELECTOR, '.VwiC3b.yXK7lf.MUxGbd').text\n",
        "    except:\n",
        "        continue\n",
        "    lines.append([title, content])\n",
        "\n",
        "lines"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qLLyzk_UTfxe"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.DataFrame(lines, columns=['title','content'])\n",
        "df\n",
        "\n",
        "df.to_csv('Google_selenium(20220809).csv')"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "02_Google_colab.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3.9.12 ('base')",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "vscode": {
      "interpreter": {
        "hash": "e4cce46d6be9934fbd27f9ca0432556941ea5bdf741d4f4d64c6cd7f8dfa8fba"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
