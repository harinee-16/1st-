{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOoTY3crpIhgX0Ebaz//iES",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/harinee-16/1st-/blob/main/1st.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8F9SEgHGqNw",
        "outputId": "c63249e4-54c9-4c10-c6c3-44e9485f2a3d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "add  16\n"
          ]
        }
      ],
      "source": [
        "a=7\n",
        "b=9\n",
        "c=a+b\n",
        "print(\"add \",c)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "a={\"name\":\"apple\",\"age\":19}\n",
        "print(a[\"name\"])\n",
        "print(a[\"age\"],\"=\",a[\"name\"])"
      ],
      "metadata": {
        "id": "yAHBSfl1b4Ia"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"computer\"\n",
        "print(a[2:5])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1KpE0ch6dHfq",
        "outputId": "e2ef8737-50a1-4dc3-9550-a80cb0af8778"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "mpu\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"computer\"\n",
        "print(a[::-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7C-jXQRudkVH",
        "outputId": "2bcd5c2f-8507-4327-bbe1-515c75876f42"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "retupmoc\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a= \"happy\"\n",
        "b= \"moring\"\n",
        "print(a+b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c9TpU_nVdu4B",
        "outputId": "df3eba51-197f-496d-9e75-465f35f34824"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "happymoring\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"colab\"\n",
        "a = a.replace(\"colab\",\"gcolab\")\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MZUBofmEeLTQ",
        "outputId": "d47209c6-0cb7-4998-c566-809c7067d7fa"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "gcolab\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"colab\"\n",
        "a = a.upper()\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MMhKQUjMetC-",
        "outputId": "d7e7c2e8-69c0-4316-e2b6-cdc67b5e14d9"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "COLAB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=\"colab\"\n",
        "a = a.startswith('c')\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UeilxtaOe4uJ",
        "outputId": "0d826900-549a-46c6-bc4a-8eccf562b6dc"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=7\n",
        "b=9\n",
        "c=a-b\n",
        "print(\"add \",c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FeL-XHSMILQM",
        "outputId": "e1205ec9-6376-48a7-8269-3483523240a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "add  -2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=int(input('enter a no a: '))\n",
        "b=int(input('enter a the no b: '))\n",
        "c=a+b\n",
        "print(\"add \",c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MsKVWL6fJUKx",
        "outputId": "6b895392-b17a-481b-bfbe-5aaf25713f47"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a no a: 12\n",
            "enter a the no b: 45\n",
            "add  57\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=7\n",
        "b=9\n",
        "c=a/b\n",
        "print(\"add \",c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M1P0tbZsJ9a_",
        "outputId": "bd31de72-c086-47d0-da29-09619a160f5b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "add  0.7777777777777778\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=int(input(\"enter a no a: \"))\n",
        "if a==50:\n",
        "  print(\"pass:\",a)\n",
        "elif a>=70:\n",
        "  print(\"average\")\n",
        "elif a>90:\n",
        "  print(\"top\")\n",
        "else:\n",
        "  print(\"fail\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GeCJ7p9SRefp",
        "outputId": "e4ba6054-cd57-4c8e-9f42-c203cf31a5dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a no a: 89\n",
            "average\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=0\n",
        "b=0\n",
        "c=\"aeior\"\n",
        "d=str(input(\"enter the word\"))\n",
        "for i in d:\n",
        "  if i in c:\n",
        "    a+=1\n",
        "    continue\n",
        "  else:\n",
        "    print(i)\n",
        "    b+=1\n",
        "print(\"vowels are :\",a)\n",
        "print(\"variables are :\",b)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3fjXRA16TOpV",
        "outputId": "db7ea1e5-d255-442c-bf69-2e4b2bddda9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the wordhappioed\n",
            "h\n",
            "p\n",
            "p\n",
            "d\n",
            "vowels are : 4\n",
            "variables are : 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range (1,10):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e7QgXZ59Uyik",
        "outputId": "88e81814-c315-4078-b795-06f0d3a3d20e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=19\n",
        "for i in range (1,12):\n",
        "  print(i)\n",
        "  s+=1\n",
        "print(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2aiI6lULU9-l",
        "outputId": "7f0dcc05-4601-4f9b-ec25-47991068a5db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "11\n",
            "30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1\")\n",
        "print(\"2\")\n",
        "print(\"3\")\n",
        "ligth=(input(\"enyer th ligth :\"))\n",
        "match(ligth):\n",
        "  case \"1\":\n",
        "    print(\"first ligth\")\n",
        "  case \"2\":\n",
        "    print(\"second lihght\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w7x_paURWs6D",
        "outputId": "dabe966f-a070-4aed-8646-6d5d8af70eac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ]
    }
  ]
}
