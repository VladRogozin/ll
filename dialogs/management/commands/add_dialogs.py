from django.core.management.base import BaseCommand
from dialogs.models import Dialog


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        data_arr = [{
  "title": {
    "english": "Hotel Room Reservation",
    "ukrainian": "Бронювання номера в готелі"
  },
  "keywords": {
    "english": ["hotel", "reservation", "room", "check-in", "amenities"],
    "ukrainian": ["готель", "бронювання", "номер", "заселення", "зручності"]
  },
  "dialog": [
    {
      "role": {
        "english": "Guest",
        "ukrainian": "Гість"
      },
      "phrase": {
        "english": "Hello! I would like to book a room for two nights. Do you have any available?",
        "ukrainian": "Вітаю! Я б хотів/хотіла забронювати номер на дві ночі. Чи є які-небудь вільні?"
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Good day! Yes, we have availability. May I know the dates of your stay?",
        "ukrainian": "Добрий день! Так, у нас є вільні номери. Чи можна дізнатися дати вашого перебування?"
      }
    },
    {
      "role": {
        "english": "Guest",
        "ukrainian": "Гість"
      },
      "phrase": {
        "english": "I plan to stay from [check-in date] to [check-out date].",
        "ukrainian": "Я планую зупинитися з [дата заселення] до [дата виселення]."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Great! We have a few options available. What type of room would you prefer, and are there any specific amenities you need?",
        "ukrainian": "Чудово! У нас є кілька варіантів. Який тип номера ви б вибрали, і чи є які-небудь конкретні зручності, які вам потрібні?"
      }
    },
    {
      "role": {
        "english": "Guest",
        "ukrainian": "Гість"
      },
      "phrase": {
        "english": "I would like a [single/double] room with [specific amenities].",
        "ukrainian": "Я б хотів/хотіла номер [одномісний/двомісний] з [конкретними зручностями]."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Certainly! Your room is booked. Could you please provide your personal details for the reservation?",
        "ukrainian": "Звісно! Ваш номер заброньовано. Можливо, ви могли б подати свої особисті дані для бронювання?"
      }
    },
    {
      "role": {
        "english": "Guest",
        "ukrainian": "Гість"
      },
      "phrase": {
        "english": "Sure, here are my details: [name], [contact information], [special requests].",
        "ukrainian": "Звісно, ось мої дані: [ім'я], [контактна інформація], [спеціальні запитання]."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Thank you! Your reservation is confirmed. We look forward to welcoming you on [check-in date].",
        "ukrainian": "Дякуємо! Ваше бронювання підтверджено. Чекаємо на вас [дата заселення]."
      }
    }
  ]
},
{
  "title": {
    "english": "Uber Ride Booking",
    "ukrainian": "Замовлення поїздки з Uber"
  },
  "keywords": {
    "english": ["Uber", "ride", "booking", "destination", "payment"],
    "ukrainian": ["Uber", "поїздка", "бронювання", "пункт призначення", "оплата"]
  },
  "dialog": [
    {
      "role": {
        "english": "Passenger",
        "ukrainian": "Пасажир"
      },
      "phrase": {
        "english": "Hello! I need to book a ride to [destination]. Are there any available Uber cars?",
        "ukrainian": "Привіт! Мені потрібно замовити поїздку до [пункт призначення]. Чи є вільні автомобілі Uber?"
      }
    },
    {
      "role": {
        "english": "Uber Driver",
        "ukrainian": "Водій Uber"
      },
      "phrase": {
        "english": "Hello! Yes, I'm available. Please provide the pickup location and confirm the destination.",
        "ukrainian": "Привіт! Так, я вільний. Будь ласка, вкажіть місце забору та підтвердіть пункт призначення."
      }
    },
    {
      "role": {
        "english": "Passenger",
        "ukrainian": "Пасажир"
      },
      "phrase": {
        "english": "I'm at [pickup location]. The destination is [destination].",
        "ukrainian": "Я зараз на [місці забору]. Пункт призначення - [пункт призначення]."
      }
    },
    {
      "role": {
        "english": "Uber Driver",
        "ukrainian": "Водій Uber"
      },
      "phrase": {
        "english": "Great! Your ride is confirmed. I'll be there in [estimated time].",
        "ukrainian": "Чудово! Ваша поїздка підтверджена. Я буду там приблизно через [приблизний час]."
      }
    },
    {
      "role": {
        "english": "Passenger",
        "ukrainian": "Пасажир"
      },
      "phrase": {
        "english": "Thank you! How can I identify your car?",
        "ukrainian": "Дякую! Як я можу впізнати ваш автомобіль?"
      }
    },
    {
      "role": {
        "english": "Uber Driver",
        "ukrainian": "Водій Uber"
      },
      "phrase": {
        "english": "Look for a [car model] with the license plate [license plate].",
        "ukrainian": "Шукайте [модель автомобіля] з номером [номерний знак]."
      }
    },
    {
      "role": {
        "english": "Passenger",
        "ukrainian": "Пасажир"
      },
      "phrase": {
        "english": "Got it! I'll be waiting.",
        "ukrainian": "Зрозуміло! Я буду чекати."
      }
    },
    {
      "role": {
        "english": "Uber Driver",
        "ukrainian": "Водій Uber"
      },
      "phrase": {
        "english": "See you soon! If you have any special requests, feel free to let me know.",
        "ukrainian": "До зустрічі незабаром! Якщо у вас є які-небудь спеціальні побажання, повідомте мені."
      }
    }
  ]
},
{
  "title": {
    "english": "Inquiring About Products in a Store",
    "ukrainian": "Запитання про товари в магазині"
  },
  "keywords": {
    "english": ["store", "products", "inquiry", "price", "availability"],
    "ukrainian": ["магазин", "товари", "запитання", "ціна", "наявність"]
  },
  "dialog": [
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Hello! I'm looking for information about some products. Can you help me?",
        "ukrainian": "Вітаю! Я шукаю інформацію про деякі товари. Чи можете ви мені допомогти?"
      }
    },
    {
      "role": {
        "english": "Store Clerk",
        "ukrainian": "Продавець-консультант"
      },
      "phrase": {
        "english": "Of course! I'm here to help. What specific products are you interested in?",
        "ukrainian": "Звісно! Я тут, щоб допомогти. Які конкретні товари вас цікавлять?"
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "I'm looking for [product 1], [product 2], and [product 3]. Can you tell me about their prices and availability?",
        "ukrainian": "Я шукаю [товар 1], [товар 2] і [товар 3]. Можете розповісти мені про їх ціни та наявність?"
      }
    },
    {
      "role": {
        "english": "Store Clerk",
        "ukrainian": "Продавець-консультант"
      },
      "phrase": {
        "english": "Certainly! [Product 1] is priced at $[price], and we have [quantity] in stock. [Product 2] is $[price] with [quantity] available. [Product 3] is currently out of stock.",
        "ukrainian": "Звісно! [Товар 1] коштує $[ціна], у нас є [кількість] на складі. [Товар 2] коштує $[ціна] з [кількість] в наявності. [Товар 3] на даний момент відсутній на складі."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Thank you for the information. Can you recommend an alternative for [out of stock product]?",
        "ukrainian": "Дякую за інформацію. Чи можете ви порекомендувати альтернативу для [відсутнього товару]?"
      }
    },
    {
      "role": {
        "english": "Store Clerk",
        "ukrainian": "Продавець-консультант"
      },
      "phrase": {
        "english": "Certainly! For [out of stock product], I recommend trying [alternative product]. It has similar features and is currently available.",
        "ukrainian": "Звісно! Для [відсутнього товару] я рекомендую спробувати [альтернативний товар]. Він має схожі характеристики і на даний момент в наявності."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Great! I'll take [quantity] of [alternative product]. Where can I find it in the store?",
        "ukrainian": "Чудово! Візьму [кількість] [альтернативний товар]. Де я можу його знайти в магазині?"
      }
    },
    {
      "role": {
        "english": "Store Clerk",
        "ukrainian": "Продавець-консультант"
      },
      "phrase": {
        "english": "It's located in aisle [number]. I can guide you there if you'd like.",
        "ukrainian": "Він розташований в ряду [номер]. Я можу вас туди провести, якщо ви хочете."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Yes, please guide me. Thank you for your assistance!",
        "ukrainian": "Так, будь ласка, проведіть мене. Дякую за вашу допомогу!"
      }
    },
    {
      "role": {
        "english": "Store Clerk",
        "ukrainian": "Продавець-консультант"
      },
      "phrase": {
        "english": "You're welcome! If you have any more questions, feel free to ask.",
        "ukrainian": "Будь ласка! Якщо у вас є ще питання, не соромтеся питати."
      }
    }
  ]
},
{
  "title": {
    "english": "Discussing Prices and Discounts",
    "ukrainian": "Обговорення цін та знижок"
  },
  "keywords": {
    "english": ["prices", "discounts", "negotiation", "offer", "final cost"],
    "ukrainian": ["ціни", "знижки", "переговори", "пропозиція", "остаточна вартість"]
  },
  "dialog": [
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Hello! I'm interested in purchasing [product/service]. Can we discuss the pricing?",
        "ukrainian": "Вітаю! Я цікавлюся покупкою [товар/послуга]. Можемо обговорити ціни?"
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "Certainly! I'm here to assist you. What specific product or service are you looking at?",
        "ukrainian": "Звісно! Я тут, щоб вам допомогти. Який конкретний товар чи послугу ви розглядаєте?"
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "[Describes the product/service]. I'm wondering about the pricing and if there are any discounts available.",
        "ukrainian": "[Описує товар/послугу]. Я цікавлюсь цінами та наявністю знижок."
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "Certainly! The regular price is $[original price]. However, we currently have a promotion, and you can get it for $[discounted price].",
        "ukrainian": "Звісно! Звичайна ціна - $[оригінальна ціна]. Але зараз у нас діє акція, і ви можете отримати його за $[знижена ціна]."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "That sounds good. Can we discuss any additional discounts or special offers?",
        "ukrainian": "Це чудово. Можемо обговорити додаткові знижки чи спеціальні пропозиції?"
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "Certainly! If you purchase [quantity], we can offer an additional [percentage] off the total cost.",
        "ukrainian": "Звісно! Якщо ви купите [кількість], ми можемо запропонувати додатково [відсоток] зі знижки на загальну вартість."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Great! I'll take [quantity]. Can you provide the final cost with all the discounts applied?",
        "ukrainian": "Чудово! Візьму [кількість]. Чи можете ви надати остаточну вартість з усіма застосованими знижками?"
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "Certainly! With the additional discount, the final cost for [quantity] would be $[final cost].",
        "ukrainian": "Звісно! З додатковою знижкою остаточна вартість за [кількість] становитиме $[остаточна вартість]."
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "That sounds reasonable. I'll proceed with the purchase. How can I make the payment?",
        "ukrainian": "Це звучить розумно. Я буду продовжувати з покупкою. Як я можу здійснити оплату?"
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "We accept [payment methods]. You can pay at the counter, and we'll provide you with a receipt. Thank you for your purchase!",
        "ukrainian": "Ми приймаємо [способи оплати]. Ви можете оплатити на касі, і ми видаємо вам квитанцію. Дякуємо за вашу покупку!"
      }
    },
    {
      "role": {
        "english": "Customer",
        "ukrainian": "Клієнт"
      },
      "phrase": {
        "english": "Thank you! I appreciate your assistance.",
        "ukrainian": "Дякую! Я вдячний/вдячна за вашу допомогу."
      }
    },
    {
      "role": {
        "english": "Salesperson",
        "ukrainian": "Продавець"
      },
      "phrase": {
        "english": "You're welcome! If you have any more questions or need further assistance, feel free to ask.",
        "ukrainian": "Будь ласка! Якщо у вас є ще питання або потрібна додаткова допомога, не соромтеся питати."
      }
    }
  ]
},
{
  "title": {
    "english": "Communication with Colleagues at Work",
    "ukrainian": "Спілкування з колегами на роботі"
  },
  "keywords": {
    "english": ["workplace", "colleagues", "communication", "team", "collaboration"],
    "ukrainian": ["робоче місце", "колеги", "спілкування", "команда", "співпраця"]
  },
  "dialog": [
    {
      "role": {
        "english": "Employee 1",
        "ukrainian": "Співробітник 1"
      },
      "phrase": {
        "english": "Good morning, everyone! I hope you had a great weekend. Is there anything new or noteworthy happening this week?",
        "ukrainian": "Доброго ранку, всім! Сподіваюся, у вас був чудовий вікенд. Чи є щось нове чи важливе цього тижня?"
      }
    },
    {
      "role": {
        "english": "Colleague 1",
        "ukrainian": "Колега 1"
      },
      "phrase": {
        "english": "Good morning! Not much, but we have a team meeting scheduled for Wednesday to discuss the upcoming project. Don't forget to prepare any updates or questions.",
        "ukrainian": "Доброго ранку! Нічого особливого, але ми маємо заплановану командну зустріч на середу для обговорення майбутнього проекту. Не забудьте підготувати будь-які оновлення чи питання."
      }
    },
    {
      "role": {
        "english": "Employee 1",
        "ukrainian": "Співробітник 1"
      },
      "phrase": {
        "english": "Thanks for the update! I'm looking forward to both the team meeting and the team-building event. If anyone has suggestions or preferences for the event, feel free to share them.",
        "ukrainian": "Дякую за оновлення! Я з нетерпінням чекаю як на командну зустріч, так і на корпоративний захід. Якщо у когось є пропозиції чи вподобання стосовно заходу, не соромтеся їх ділитися."
      }
    },
    {
      "role": {
        "english": "Colleague 1",
        "ukrainian": "Колега 1"
      },
      "phrase": {
        "english": "Certainly! I believe it's essential for the team to actively participate and contribute to make the event enjoyable for everyone.",
        "ukrainian": "Звісно! Я вважаю, що важливо, щоб команда активно брала участь і вносила свій внесок, щоб захід був приємним для всіх."
      }
    },
    {
      "role": {
        "english": "Employee 1",
        "ukrainian": "Співробітник 1"
      },
      "phrase": {
        "english": "Absolutely! Team spirit plays a significant role in our success. Looking forward to a productive and enjoyable week with all of you!",
        "ukrainian": "Звісно! Командний дух відіграє важливу роль у нашому успіху. Чекаю на продуктивний та приємний тиждень з вами всіма!"
      }
    }
  ]
},
{
  "title": {
    "english": "Discussing Project with the Supervisor",
    "ukrainian": "Обговорення проекту з начальником"
  },
  "keywords": {
    "english": ["project", "discussion", "supervisor", "progress", "feedback"],
    "ukrainian": ["проект", "обговорення", "начальник", "прогрес", "відгук"]
  },
  "dialog": [
    {
      "role": {
        "english": "Employee",
        "ukrainian": "Співробітник"
      },
      "phrase": {
        "english": "Good morning, [Supervisor's Name]! I'd like to discuss the progress and updates on [Project Name]. Do you have a moment?",
        "ukrainian": "Доброго ранку, [Ім'я начальника]! Я б хотів/хотіла обговорити прогрес та оновлення щодо [Назва проекту]. У вас є хвилина?"
      }
    },
    {
      "role": {
        "english": "Supervisor",
        "ukrainian": "Начальник"
      },
      "phrase": {
        "english": "Good morning! Of course, let's discuss. How is the project progressing, and do you have any challenges or achievements to share?",
        "ukrainian": "Доброго ранку! Звісно, давайте обговоримо. Як прогресує проект, і чи є у вас які-небудь труднощі чи досягнення для обговорення?"
      }
    },
    {
      "role": {
        "english": "Employee",
        "ukrainian": "Співробітник"
      },
      "phrase": {
        "english": "The project is moving forward steadily. We've completed [specific tasks] and are currently working on [next steps]. I'd like to share our achievements in [aspect of the project].",
        "ukrainian": "Проект рухається вперед стійко. Ми вже завершили [конкретні завдання] і зараз працюємо над [наступні кроки]. Я хочу поділитися нашими досягненнями в [аспект проекту]."
      }
    },
    {
      "role": {
        "english": "Supervisor",
        "ukrainian": "Начальник"
      },
      "phrase": {
        "english": "That's great to hear! I appreciate your hard work. Are there any areas where you need additional support or resources?",
        "ukrainian": "Чудово чути! Я вдячний/вдячна за вашу працю. Чи є які-небудь області, де вам потрібна додаткова підтримка чи ресурси?"
      }
    },
    {
      "role": {
        "english": "Employee",
        "ukrainian": "Співробітник"
      },
      "phrase": {
        "english": "We're doing well overall, but there's a specific challenge related to [challenge description]. I wanted to discuss possible solutions and get your input.",
        "ukrainian": "В цілому у нас все йде добре, але є конкретна трудність пов'язана з [опис труднощів]. Я хотів/хотіла обговорити можливі рішення та отримати ваші вказівки."
      }
    },
    {
      "role": {
        "english": "Supervisor",
        "ukrainian": "Начальник"
      },
      "phrase": {
        "english": "I appreciate your proactive approach in addressing challenges. Let's discuss potential solutions, and I'll provide guidance on how to overcome this obstacle.",
        "ukrainian": "Я вдячний/вдячна за вашу ініціативу в роботі над труднощами. Давайте обговоримо можливі рішення, і я надам вам вказівки, як подолати цю перешкоду."
      }
    },
    {
      "role": {
        "english": "Employee",
        "ukrainian": "Співробітник"
      },
      "phrase": {
        "english": "Thank you, [Supervisor's Name]! I value your guidance. Additionally, I wanted to discuss [any additional topics or requests related to the project].",
        "ukrainian": "Дякую, [Ім'я начальника]! Я ціную ваші вказівки. Крім того, я хотів/хотіла обговорити [будь-які додаткові теми чи запитання, пов'язані з проектом]."
      }
    },
    {
      "role": {
        "english": "Supervisor",
        "ukrainian": "Начальник"
      },
      "phrase": {
        "english": "Certainly! Feel free to bring up any additional topics. I'm here to support you and ensure the project's success.",
        "ukrainian": "Звісно! Не соромтеся вносити будь-які додаткові теми. Я тут, щоб вас підтримати та забезпечити успіх проекту."
      }
    }
  ]
},
{
  "title": {
    "english": "Scheduling an Appointment with the Doctor",
    "ukrainian": "Запис на прийом до лікаря"
  },
  "keywords": {
    "english": ["appointment", "doctor", "healthcare", "schedule", "medical"],
    "ukrainian": ["прийом", "лікар", "охорона здоров'я", "розклад", "медичний"]
  },
  "dialog": [
    {
      "role": {
        "english": "Patient",
        "ukrainian": "Пацієнт"
      },
      "phrase": {
        "english": "Hello, I would like to schedule an appointment with Dr. [Doctor's Name]. I've been experiencing [brief description of symptoms]. Can you help me with that?",
        "ukrainian": "Вітаю, я б хотів/хотіла записатися на прийом до доктора [Ім'я лікаря]. У мене виникли [короткий опис симптомів]. Чи можете ви мені допомогти з цим?"
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Good day! Certainly, I can assist you with that. May I have your full name, date of birth, and contact number, please?",
        "ukrainian": "Добрий день! Звісно, я можу вам у цьому допомогти. Назвіть, будь ласка, ваше повне ім'я, дату народження та контактний номер."
      }
    },
    {
      "role": {
        "english": "Patient",
        "ukrainian": "Пацієнт"
      },
      "phrase": {
        "english": "Certainly, my name is [Full Name], my date of birth is [Date of Birth], and you can reach me at [Contact Number].",
        "ukrainian": "Звісно, мене звуть [Повне ім'я], моя дата народження - [Дата народження], і ви можете зв'язатися зі мною за номером [Контактний номер]."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Thank you, [Full Name]. I see there are available slots on [available dates]. Please choose a convenient date and time for your appointment.",
        "ukrainian": "Дякую, [Повне ім'я]. Я бачу вільні слоти на [доступні дати]. Будь ласка, оберіть зручну дату та час для вашого прийому."
      }
    },
    {
      "role": {
        "english": "Patient",
        "ukrainian": "Пацієнт"
      },
      "phrase": {
        "english": "I would prefer an appointment on [chosen date] at [chosen time], if available.",
        "ukrainian": "Я б віддав перевагу прийому [обрана дата] о [обраний час], якщо це можливо."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "Certainly, [Full Name]! Your appointment with Dr. [Doctor's Name] is confirmed on [chosen date] at [chosen time]. If you have any urgent concerns before the appointment, feel free to contact us.",
        "ukrainian": "Звісно, [Повне ім'я]! Ваш прийом до доктора [Ім'я лікаря] підтверджено на [обрана дата] о [обраний час]. Якщо у вас є які-небудь термінові питання перед прийомом, не соромтеся зв'язатися з нами."
      }
    },
    {
      "role": {
        "english": "Patient",
        "ukrainian": "Пацієнт"
      },
      "phrase": {
        "english": "Thank you for your assistance! I look forward to my appointment.",
        "ukrainian": "Дякую за вашу допомогу! Я з нетерпінням чекаю свого прийому."
      }
    },
    {
      "role": {
        "english": "Receptionist",
        "ukrainian": "Адміністратор"
      },
      "phrase": {
        "english": "You're welcome, [Full Name]! If you have any further questions or need assistance, feel free to contact us. Have a great day!",
        "ukrainian": "Будь ласка, [Повне ім'я]! Якщо у вас є ще які-небудь питання або потребуєте допомоги, не соромтеся звертатися до нас. Гарного вам дня!"
      }
    }
  ]
},
{
  "title": {
    "english": "Discussing Symptoms and Seeking Advice",
    "ukrainian": "Обговорення симптомів та отримання порад"
  },
  "keywords": {
    "english": ["symptoms", "health", "advice", "medical", "consultation"],
    "ukrainian": ["симптоми", "здоров'я", "поради", "медичний", "консультація"]
  },
  "dialog": [
    {
      "role": {
        "english": "Individual",
        "ukrainian": "Особа"
      },
      "phrase": {
        "english": "Hello, I've been experiencing [brief description of symptoms]. I'm a bit concerned and was wondering if you could provide some advice or insights.",
        "ukrainian": "Вітаю, у мене виникли [короткий опис симптомів]. Я трошки хвилююсь і хотів/хотіла б дізнатися, чи можете ви надати які-небудь поради чи вказівки."
      }
    },
    {
      "role": {
        "english": "Advisor",
        "ukrainian": "Консультант"
      },
      "phrase": {
        "english": "Hello! I'm here to help. I understand it can be concerning. Can you provide more details about the symptoms? Have you noticed any specific patterns or triggers?",
        "ukrainian": "Вітаю! Я тут, щоб допомогти. Розумію, що це може вас турбувати. Чи можете ви надати більше деталей щодо симптомів? Чи помітили ви які-небудь конкретні закономірності чи спричинювачі?"
      }
    },
    {
      "role": {
        "english": "Individual",
        "ukrainian": "Особа"
      },
      "phrase": {
        "english": "Certainly, the symptoms include [more detailed description]. I haven't identified specific patterns, but they started around [timeframe].",
        "ukrainian": "Звісно, серед симптомів є [більш детальний опис]. Я не виявив/виявила конкретних закономірностей, але вони почалися приблизно [період часу]."
      }
    },
    {
      "role": {
        "english": "Advisor",
        "ukrainian": "Консультант"
      },
      "phrase": {
        "english": "Thank you for sharing that information. While I'm not a medical professional, I can offer some general advice. It's important to [general advice]. However, I recommend consulting with a healthcare professional for a more accurate assessment.",
        "ukrainian": "Дякую за надану інформацію. Хоча я не є медичним фахівцем, я можу запропонувати загальні поради. Важливо [загальні поради]. Однак рекомендую звернутися до медичного фахівця для більш точної оцінки."
      }
    },
    {
      "role": {
        "english": "Individual",
        "ukrainian": "Особа"
      },
      "phrase": {
        "english": "I appreciate your advice. I'll consider [general advice] and seek professional medical advice as well. If the symptoms persist, I'll consult with a healthcare professional.",
        "ukrainian": "Я ціную ваші поради. Я буду враховувати [загальні поради] і також звернусь до професійного медичного консультанта. Якщо симптоми не зникають, я звернусь до медичного фахівця."
      }
    },
    {
      "role": {
        "english": "Advisor",
        "ukrainian": "Консультант"
      },
      "phrase": {
        "english": "That sounds like a reasonable plan. If you have any further questions or if the situation changes, feel free to reach out. Take care of yourself!",
        "ukrainian": "Це звучить як розумний план. Якщо у вас є ще які-небудь питання або якщо ситуація зміниться, не соромтеся звертатися. Дбайте про себе!"
      }
    },
    {
      "role": {
        "english": "Individual",
        "ukrainian": "Особа"
      },
      "phrase": {
        "english": "Thank you for your understanding and guidance. I'll stay attentive to any changes and seek professional help if needed. Have a great day!",
        "ukrainian": "Дякую за вашу розуміння та вказівки. Я буду уважно відноситися до будь-яких змін і звертатися за професійною допомогою, якщо це буде необхідно. Гарного вам дня!"
      }
    }
  ]
},
{
  "title": {
    "english": "Course or Lecture Registration",
    "ukrainian": "Реєстрація на курси або лекції"
  },
  "keywords": {
    "english": ["registration", "course", "lecture", "enrollment", "education"],
    "ukrainian": ["реєстрація", "курс", "лекція", "зареєструватися", "освіта"]
  },
  "dialog": [
    {
      "role": {
        "english": "Participant",
        "ukrainian": "Учасник"
      },
      "phrase": {
        "english": "Hello, I'm interested in registering for the [Course/Lecture Name]. Can you provide information on the registration process and any requirements?",
        "ukrainian": "Доброго дня, мене цікавить реєстрація на [Назва курсу/лекції]. Чи можете ви надати інформацію щодо процесу реєстрації та всіх вимог?"
      }
    },
    {
      "role": {
        "english": "Registrar",
        "ukrainian": "Реєстратор"
      },
      "phrase": {
        "english": "Hello! Certainly, I can assist you with the registration process. To start, could you please provide your full name, contact details, and any relevant background or prerequisites?",
        "ukrainian": "Вітаю! Звісно, я можу вам допомогти з процесом реєстрації. Спочатку, будь ласка, надайте своє повне ім'я, контактні дані та будь-яку відповідну інформацію чи передумови."
      }
    },
    {
      "role": {
        "english": "Participant",
        "ukrainian": "Учасник"
      },
      "phrase": {
        "english": "Certainly, my name is [Full Name], and you can reach me at [Contact Details]. I have [briefly mention any relevant background or prerequisites].",
        "ukrainian": "Звісно, мене звуть [Повне ім'я], і ви можете зв'язатися зі мною за [Контактні дані]. У мене є [коротко вказати будь-які відповідні підготовка або передумови]."
      }
    },
    {
      "role": {
        "english": "Registrar",
        "ukrainian": "Реєстратор"
      },
      "phrase": {
        "english": "Thank you for providing that information, [Full Name]. You are now successfully registered for the [Course/Lecture Name]. Additionally, here are details regarding the schedule and materials. If you have any questions, feel free to ask.",
        "ukrainian": "Дякую за надану інформацію, [Повне ім'я]. Ви успішно зареєстровані на [Назва курсу/лекції]. Додатково, ось деталі щодо розкладу та матеріалів. Якщо у вас є питання, не соромтеся питати."
      }
    },
    {
      "role": {
        "english": "Participant",
        "ukrainian": "Учасник"
      },
      "phrase": {
        "english": "Great! I appreciate your assistance. Could you provide information on any pre-course materials or preparations I should consider?",
        "ukrainian": "Чудово! Я ціную вашу допомогу. Чи можете ви надати інформацію щодо будь-яких попередніх матеріалів чи підготовки, яку мені варто розглянути?"
      }
    },
    {
      "role": {
        "english": "Registrar",
        "ukrainian": "Реєстратор"
      },
      "phrase": {
        "english": "Certainly, [Full Name]! Here are the pre-course materials and recommended preparations [provide details]. If you have any further queries, feel free to reach out.",
        "ukrainian": "Звісно, [Повне ім'я]! Ось попередні матеріали та рекомендовані підготовки [надати деталі]. Якщо у вас є ще які-небудь питання, не соромтеся звертатися."
      }
    },
    {
      "role": {
        "english": "Participant",
        "ukrainian": "Учасник"
      },
      "phrase": {
        "english": "Thank you for the information. I'm looking forward to the [Course/Lecture]. If there's anything else I need to know, I'll be sure to ask. Have a wonderful day!",
        "ukrainian": "Дякую за інформацію. Я з нетерпінням чекаю [Назва курсу/лекції]. Якщо є щось ще, що мені варто знати, обов'язково запитаю. Гарного вам дня!"
      }
    },
    {
      "role": {
        "english": "Registrar",
        "ukrainian": "Реєстратор"
      },
      "phrase": {
        "english": "You're welcome, [Full Name]! If you have any further questions or need assistance, feel free to contact us. Enjoy your learning journey!",
        "ukrainian": "Будь ласка, [Повне ім'я]! Якщо у вас є ще які-небудь питання чи потрібна допомога, не соромтеся звертатися до нас. Насолоджуйтеся вашим навчальним шляхом!"
      }
    }
  ]
},
{
  "title": {
    "english": "Communication with the Teacher",
    "ukrainian": "Спілкування з викладачем"
  },
  "keywords": {
    "english": ["communication", "teacher", "inquiry", "clarification", "feedback"],
    "ukrainian": ["спілкування", "викладач", "запитання", "роз'яснення", "зворотний зв'язок"]
  },
  "dialog": [
    {
      "role": {
        "english": "Student",
        "ukrainian": "Студент"
      },
      "phrase": {
        "english": "Hello, I have a question regarding the recent lecture on [topic]. Could you provide some clarification or additional information on [specific point]?",
        "ukrainian": "Добрий день, у мене є питання щодо останньої лекції на тему [тема]. Чи можете ви надати роз'яснення чи додаткову інформацію щодо [конкретний пункт]?"
      }
    },
    {
      "role": {
        "english": "Teacher",
        "ukrainian": "Викладач"
      },
      "phrase": {
        "english": "Hello! Of course, I'd be happy to help. Could you please specify which part of the lecture or topic you're referring to? I'll do my best to provide the information you need.",
        "ukrainian": "Вітаю! Звісно, я буду радий допомогти. Можете вказати, на яку частину лекції чи тему ви посилаєтеся? Я зроблю все можливе, щоб надати вам необхідну інформацію."
      }
    },
    {
      "role": {
        "english": "Student",
        "ukrainian": "Студент"
      },
      "phrase": {
        "english": "Certainly, I was particularly interested in the section about [specific concept]. Could you elaborate on [specific question or aspect]?",
        "ukrainian": "Звісно, мене особливо зацікавила секція щодо [конкретна концепція]. Чи можете ви розгорнути [конкретне питання чи аспект]?"
      }
    },
    {
      "role": {
        "english": "Teacher",
        "ukrainian": "Викладач"
      },
      "phrase": {
        "english": "Certainly. [Elaborate on the specific concept or provide additional information]. I hope that clarifies your question. If you have any more inquiries, feel free to ask.",
        "ukrainian": "Звісно. [Розгорнути конкретну концепцію або надати додаткову інформацію]. Сподіваюся, це роз'яснює ваше питання. Якщо у вас є ще які-небудь питання, не соромтеся питати."
      }
    },
    {
      "role": {
        "english": "Student",
        "ukrainian": "Студент"
      },
      "phrase": {
        "english": "Thank you for the clarification. I appreciate your help. Additionally, do you have any recommendations for further reading or resources on [related topic]?",
        "ukrainian": "Дякую за роз'яснення. Я вдячний/вдячна за вашу допомогу. Додатково, чи є у вас рекомендації щодо додаткового читання чи ресурсів щодо [пов'язана тема]?"
      }
    },
    {
      "role": {
        "english": "Teacher",
        "ukrainian": "Викладач"
      },
      "phrase": {
        "english": "You're welcome! I'm glad I could assist you. Certainly, here are some recommended readings and resources on [related topic] [provide details]. Feel free to explore them for a more in-depth understanding.",
        "ukrainian": "Будь ласка! Я радий/рада був допомогти вам. Звісно, ось кілька рекомендованих читань та ресурсів щодо [пов'язана тема] [надати деталі]. Відчуйте себе вільними досліджувати їх для більш глибокого розуміння."
      }
    },
    {
      "role": {
        "english": "Student",
        "ukrainian": "Студент"
      },
      "phrase": {
        "english": "Thank you so much for your guidance. I'll explore those resources. If I have any more questions or need further clarification, I'll reach out. Have a wonderful day!",
        "ukrainian": "Дуже дякую за вашу допомогу. Я вивчу ці ресурси. Якщо у мене буде ще які-небудь питання або потрібне додаткове роз'яснення, я звернуся. Гарного вам дня!"
      }
    },
    {
      "role": {
        "english": "Teacher",
        "ukrainian": "Викладач"
      },
      "phrase": {
        "english": "You're welcome, [Student's Name]! Feel free to reach out anytime. I'm here to help. Have a successful learning journey!",
        "ukrainian": "Будь ласка, [Ім'я Студента]! Не соромтеся звертатися в будь-який час. Я тут, щоб допомогти. Нехай ваш навчальний шлях буде успішним!"
      }
    }
  ]
}
]

        for data in data_arr:
            new_instance = Dialog(
                title=data["title"],
                keywords=data["keywords"],
                dialog=data["dialog"],
            )
            new_instance.save()

        print(len(data_arr))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))
