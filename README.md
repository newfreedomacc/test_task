# test_task
Я понимаю, что код нуждается в доработке.  
Во-первых, нужно ловить исключения и на их основании делать фиксирование несоответствий. Я видел конструкцию через try. Не вдавался в подробности, но подозреваю, что часть кода с assert или WebDriverWait мы выносим в блок try и при вылете исключения, просто индексируем его (делаем скрин или другое подобное действие) и просто идйм дальше.  
  
Во-вторых, я не разделял на классы. Я это вижу как оптимизацию кода, когда я использую подключаю готовые модули к текущему проекту. Похожую мысль видел в статье на хабре, к которой я обращался при подготовке задания. Но данное задание несло скорее исследовательский характер, поэтому смысла усложнять себе работу я не увидел.  
  
Ну и в целом я пока не могу критически просмотреть свой код, я не абстрагировался от текущего задания и над другими не работал (свои проверки работы методов не в счёт). У меня есть вопросы по паре моментов, но думаю в процессе углубления в материал я получу на них ответы.  
