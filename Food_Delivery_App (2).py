{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fInbjE15H_Wm",
        "outputId": "5d38cc4a-605f-4900-ab52-c64735cd5616"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<----Enter Detail Pizza---->\n",
            "<----Enter Detail Burger---->\n"
          ]
        },
        {
          "ename": "ValueError",
          "evalue": "invalid literal for int() with base 10: ''",
          "output_type": "error",
          "traceback": [
            "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
            "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
            "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 82\u001b[39m\n\u001b[32m     78\u001b[39m price=int(input(\u001b[33m\"Enter price:\"\u001b[39m))\n\u001b[32m     79\u001b[39m pizza = Pizza(name,price)\n\u001b[32m     80\u001b[39m print(\u001b[33m\"<----Enter Detail Burger---->\"\u001b[39m)\n\u001b[32m     81\u001b[39m name=str(input(\u001b[33m\"Enter name item:\"\u001b[39m))\n\u001b[32m---> \u001b[39m\u001b[32m82\u001b[39m price=int(input(\u001b[33m\"Enter price:\"\u001b[39m))\n\u001b[32m     83\u001b[39m burger = Burger(name, price)\n\u001b[32m     84\u001b[39m print(\u001b[33m\"<----Enter Detail Biryani---->\"\u001b[39m)\n\u001b[32m     85\u001b[39m name=str(input(\u001b[33m\"Enter name item:\"\u001b[39m))\n",
            "\u001b[31mValueError\u001b[39m: invalid literal for int() with base 10: ''"
          ]
        }
      ],
      "source": [
        "# Food Delivery Management System\n",
        "\n",
        "class Food:\n",
        "    def __init__(self, name, price):\n",
        "        self.name = name\n",
        "        self.price = price\n",
        "\n",
        "    def calculate_price(self):\n",
        "        return self.price\n",
        "\n",
        "    def display(self):\n",
        "        print(\"Food:\", self.name)\n",
        "        print(\"Price:\", self.price)\n",
        "\n",
        "\n",
        "# Child Class 1\n",
        "class Pizza(Food):\n",
        "    def calculate_price(self):\n",
        "        # Pizza has 10% discount\n",
        "        return self.price - (self.price * 0.10)\n",
        "\n",
        "\n",
        "# Child Class 2\n",
        "class Burger(Food):\n",
        "    def calculate_price(self):\n",
        "        # Burger has 5% discount\n",
        "        return self.price - (self.price * 0.05)\n",
        "\n",
        "\n",
        "# Child Class 3\n",
        "class Biryani(Food):\n",
        "    def calculate_price(self):\n",
        "        # Biryani has 8% discount\n",
        "        return self.price - (self.price * 0.08)\n",
        "\n",
        "\n",
        "# Order Class\n",
        "class Order:\n",
        "    def __init__(self):\n",
        "        self.food_items = []\n",
        "\n",
        "    def add_food(self, food):\n",
        "        self.food_items.append(food)\n",
        "        print(food.name, \"added to order.\")\n",
        "\n",
        "    def remove_food(self, name):\n",
        "        for food in self.food_items:\n",
        "            if food.name.lower() == name.lower():\n",
        "                self.food_items.remove(food)\n",
        "                print(food.name, \"removed from order.\")\n",
        "                return\n",
        "\n",
        "        print(\"Food item not found.\")\n",
        "\n",
        "    def calculate_total(self):\n",
        "        total = 0\n",
        "\n",
        "        for food in self.food_items:\n",
        "            total += food.calculate_price()\n",
        "\n",
        "        return total\n",
        "\n",
        "    def display_order(self):\n",
        "        print(\"\\n----- Order Details -----\")\n",
        "\n",
        "        if len(self.food_items) == 0:\n",
        "            print(\"Order is empty.\")\n",
        "            return\n",
        "\n",
        "        for food in self.food_items:\n",
        "            print(food.name, \"-> Rs.\", food.calculate_price())\n",
        "\n",
        "        print(\"-------------------------\")\n",
        "        print(\"Total Bill: Rs.\", self.calculate_total())\n",
        "# Create Food Objects\n",
        "print(\"<----Enter Detail Pizza---->\")\n",
        "name=str(input(\"Enter name item:\"))\n",
        "price=int(input(\"Enter price:\"))\n",
        "pizza = Pizza(name,price)\n",
        "print(\"<----Enter Detail Burger---->\")\n",
        "name=str(input(\"Enter name item:\"))\n",
        "price=int(input(\"Enter price:\"))\n",
        "burger = Burger(name, price)\n",
        "print(\"<----Enter Detail Biryani---->\")\n",
        "name=str(input(\"Enter name item:\"))\n",
        "price=int(input(\"Enter price:\"))\n",
        "biryani = Biryani(name, price)\n",
        "\n",
        "# Create Order\n",
        "order = Order()\n",
        "# Add food items\n",
        "order.add_food(pizza)\n",
        "order.add_food(burger)\n",
        "order.add_food(biryani)\n",
        "# Display Order\n",
        "order.display_order()\n",
        "# Remove Food\n",
        "order.remove_food(\"Burger\")\n",
        "# Display Updated Order\n",
        "order.display_order()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
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
      "version": "3.15.0rc2"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
