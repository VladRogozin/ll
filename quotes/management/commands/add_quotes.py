from django.core.management.base import BaseCommand
from quotes.models import Quote


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        data_arr = [
          {
            "original": "Your time is limited, don't waste it living someone else's life.",
            "translation": "Твій час обмежений, не витрачай його, живучи життям іншої людини.",
            "author": "Steve Jobs"
          },
          {
            "original": "Life is really simple, but we insist on making it complicated.",
            "translation": "Життя дійсно просте, але ми настоюємо на тому, щоб ускладнювати його.",
            "author": "Confucius"
          },
          {
            "original": "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change.",
            "translation": "Не найсильніші види виживають, не найрозумніші, а ті, що найбільше реагують на зміни.",
            "author": "Charles Darwin"
          },
          {
            "original": "You don't have to be rich to sparkle.",
            "translation": "Ви не повинні бути багатими, щоб блищати.",
            "author": "Невідомий"
          },
          {
            "original": "A journey of a thousand miles begins with a single step.",
            "translation": "Подорож тисячі миль починається з одного кроку.",
            "author": "Lao Tzu"
          },
          {
            "original": "The only limit to our realization of tomorrow will be our doubts of today.",
            "translation": "Єдиним обмеженням нашої реалізації завтра буде наш сумнів сьогодення.",
            "author": "Franklin D. Roosevelt"
          },
          {
            "original": "Success is liking yourself, liking what you do, and liking how you do it.",
            "translation": "Успіх - це подобатися собі, те, що ти робиш, і те, як ти це робиш.",
            "author": "Maya Angelou"
          },
          {
            "original": "Do what you can, with what you have, where you are.",
            "translation": "Робіть те, що ви можете, з тим, що у вас є, там, де ви знаходитесь.",
            "author": "Theodore Roosevelt"
          },
          {
            "original": "The purpose of our lives is to add value to the people of this generation and those that follow.",
            "translation": "Мета наших життів - додавати цінність людям цього покоління і тим, що йдуть за ним.",
            "author": "Buckminster Fuller"
          },
          {
            "original": "You are the average of the five people you spend the most time with.",
            "translation": "Ви - середнє значення п'ятерох людей, з якими ви проводите найбільше часу.",
            "author": "Jim Rohn"
          },
          {
            "original": "Life is 10% what happens to us and 90% how we react to it.",
            "translation": "Життя - це 10% те, що трапляється з нами і 90% те, як ми реагуємо на це.",
            "author": "Charles R. Swindoll"
          },
          {
            "original": "The best way to predict your future is to create it.",
            "translation": "Найкращий спосіб передбачити свій майбутній - це створити його.",
            "author": "Peter Drucker"
          },
          {
            "original": "You never fail until you stop trying.",
            "translation": "Ви не зазнаєте невдачі, поки не перестанете намагатися.",
            "author": "Albert Einstein"
          },
          {
            "original": "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.",
            "translation": "Єдине, що стоїть між вами і вашою метою, - це історія, яку ви продовжуєте розповідати собі про те, чому ви не можете її досягти.",
            "author": "Jordan Belfort"
          },
          {
            "original": "Happiness is not in the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort.",
            "translation": "Щастя не полягає лише в володінні грошима; воно полягає в радості вдосягнень, в захваті творчих зусиль.",
            "author": "Franklin D. Roosevelt"
          },
          {
            "original": "Don't count the days, make the days count.",
            "translation": "Не лічте дні, робіть дні важливими.",
            "author": "Muhammad Ali"
          },
          {
            "original": "You can never cross the ocean until you have the courage to lose sight of the shore.",
            "translation": "Ви ніколи не перетнете океан, поки не наберетесь мужності втратити зоровий контакт з берегом.",
            "author": "Christopher Columbus"
          },
          {
            "original": "The only person you are destined to become is the person you decide to be.",
            "translation": "Єдиною людиною, на яку ви призначені стати, є та, ким ви вирішите бути.",
            "author": "Ralph Waldo Emerson"
          },
          {
            "original": "The best revenge is to be unlike him who performed the injustice.",
            "translation": "Найкраща помста - бути неподібним тому, хто вчинив несправедливість.",
            "author": "Marcus Aurelius"
          },
          {
            "original": "It always seems impossible until it's done.",
            "translation": "Завжди здається неможливим, поки не зроблено.",
            "author": "Nelson Mandela"
          },
          {
            "original": "Strive not to be a success, but rather to be of value.",
            "translation": "Прагніть не до успіху, а до того, щоб бути цінним.",
            "author": "Albert Einstein"
          },
          {
            "original": "The only limit to our realization of tomorrow will be our doubts of today.",
            "translation": "Єдиним обмеженням нашої реалізації завтра буде наш сумнів сьогодення.",
            "author": "Franklin D. Roosevelt"
          },
          {
            "original": "The future belongs to those who believe in the beauty of their dreams.",
            "translation": "Майбутнє належить тим, хто вірить в красу своїх мрій.",
            "author": "Eleanor Roosevelt"
          },
          {
            "original": "You can't cross the sea merely by standing and staring at the water.",
            "translation": "Ви не перетнете море, просто стоячи і дивлячись на воду.",
            "author": "Rabindranath Tagore"
          },
          {
            "original": "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
            "translation": "Те, що лежить за нами і те, що лежить перед нами, - це дрібниці порівняно з тим, що лежить у нас всередині.",
            "author": "Ralph Waldo Emerson"
          },
          {
            "original": "Sometimes the questions are complicated, and the answers are simple.",
            "translation": "Іноді питання складні, а відповіді - прості.",
            "author": "Dr. Seuss"
          },
          {
            "original": "Be the change that you wish to see in the world.",
            "translation": "Будьте зміною, яку ви хочете бачити у світі.",
            "author": "Mahatma Gandhi"
          },
          {
            "original": "In the end, we will remember not the words of our enemies, but the silence of our friends.",
            "translation": "У кінці ми будемо пам'ятати не слова наших ворогів, а мовчання наших друзів.",
            "author": "Martin Luther King Jr."
          },
          {
            "original": "The only way to do great work is to love what you do.",
            "translation": "Єдиний спосіб робити велику роботу - це любити те, що ти робиш.",
            "author": "Steve Jobs"
          },
          {
            "original": "Live as if you were to die tomorrow. Learn as if you were to live forever.",
            "translation": "Живіть, ніби ви маєте померти завтра. Вчіться, ніби ви маєте жити вічно.",
            "author": "Mahatma Gandhi"
          }

        ]

        for data in data_arr:
            new_instance = Quote(
                original=data["original"],
                translation=data["translation"],
                author=data["author"],
            )
            new_instance.save()

        print(len(data_arr))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))
