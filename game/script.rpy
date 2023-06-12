# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")
define s = Character("Fellow Student")
define y = Character("You")
define d = Character("Developer")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "我迫不及待地想知道Stable Diffusion是如何工作的！"

    "而且这个 ComfyUI 看起来真的很棒！"

    "我走进教室。"

    scene teacher grin with fade

    "我看着身边。"

    scene student happy with fade

    "这地方不错。"

label basic_tutorial:
    scene teacher happy with fade

    t "现在，让我们开始吧"

    t "我们首先要讨论的是模型文件(model files)"

    t "您从Huggingface或Civitai下载的大文件。"

    t "这些大型.ckpt或.safetensors文件到底包含什么？"

    t "它们包含3种不同模型的权重: CLIP、主模型和 VAE。"

    #t "Stable Diffusion MODEL 的另一个名称是 UNET。"

    show comfyui checkpointloader at topleft

    t "在默认的ComfyUI工作流程中，这里由CheckpointLoader表示。"

    t "它允许您选择要加载的检查点(checkpoint)。"

    t "您将注意到它有3个不同的输出: MODEL(模型)、 CLIP、 VAE"

    show comfyui cliptextencode at topleft

    t "让我们从 CLIP 模型开始"

    t "CLIP 模型连接到 CLIPTextEncode 节点。"

    t "在Stable Diffusion中，CLIP 用于将文本编码为主 MODEL 可以理解的格式。"

    t "这就是为什么它的另一个名称是文本编码器。"

    show comfyui sampler at topleft
    
    t "在stable diffusion中，图像是使用我们所说的采样器生成的"

    show comfyui sampler_arrow at topleft

    t "在 ComfyUI 中，这由采样器(sampler)节点表示。"

    t "采样器(sampler)采用Stable Diffusion主模型作为输入。"

    show comfyui sampler_arrow_clip at topleft

    t "它还接受由 CLIP模型 编码的正面和负面提示。"

    show comfyui sampler_arrow_latent at topleft

    t "它需要的最后输入是潜在图像(Latent Image)。"

    t "因为我们只从文本(txt2img)生成图像，所以我们传递给它一个空图像。"

    show comfyui sampler_arrow at topleft

    t "采样器(sampler)获取输入的潜在图像，为它添加噪声，然后使用主模型对其进行去噪。"

    t "在每个采样步骤中，编码的正提示和负提示被传递给 主模型 ，并用于指导去噪。"

    show comfyui sampler at topleft

    t "这种渐进的去噪是Stable Diffusion产生图像的方式。"

    t "采样器(sampler)输出去噪后的图像。"

    show comfyui vaedecode at topleft

    t "stable diffusion使用的第三个也是最后一个模型是VAE。"

    t "VAE 用于将图像从潜在空间转换为像素空间。"

    t "潜在空间是Stable Diffusion主模型理解的格式，而像素空间是图像查看器理解的格式。"

    show comfyui vaedecode_arrow at topleft

    t "您可以在这里看到，VAEDecode 节点将来自采样器的潜在图像作为输入并输出一个常规图像。"

    show comfyui vaedecode_arrow_save at topleft

    t "然后将图像保存到带有SaveImage节点的PNG文件中。"

    scene black with fade

    show comfyui basicworkflow at top

    t "这就是一个基本且完整的文字转图像的工作流程了."

    scene teacher grin with fade

    t "有什么问题吗?"

label q1:
    menu:

        "我有个问题"

        "你能重复一遍吗？我没明白。":

            jump repeat

        "我爱你!":

            jump love

        "没问题,俺晓得了":

            jump understand

label repeat:
    scene teacher grin

    t "当然，这就是我来这儿的目的"

    jump basic_tutorial

label love:
    scene teacher surprised

    t "这不是个问题。"

    scene teacher blush

    t "这只是一个 ComfyUI 教程，请不要转移话题。"
    jump q1

label understand:

    scene teacher happy

    t "太好了，那我们另一个学生呢？"

    scene student crying with fade

    s "我什么都不明白。"

    s "太复杂了"

    scene student angry

    s "这太难了! ! ！"

    scene teacher grin with fade

    t "好吧，我得走了，所以你应该帮帮她。"

    scene student happy with fade

    s "你会帮我的，对吗？"

label q2:
    menu:

        "我该怎么办"

        "我帮她。":

            jump help_her

        "不关我的事。":

            jump not_my_problem

        "公平地说，你需要像我一样拥有高智商才能理解 Stable Diffusion.":

            jump high_iq

label not_my_problem:

    y "不关我的事。"

    scene student angry

    s "...."

    scene student crying

    s "...."

    scene black with fade

    "我走了"

    jump tutorial_2

label help_her:
    y "我当然会帮你，你不明白什么？"

    scene student blush

    s "所有的"

    "好吧，这可能要花点时间..。"

    jump tutorial_2

label high_iq:
    y "我的智商很高，所以我想我有责任帮助那些像你这样头脑低的人。"

    s "...."

    scene student grin

    s "你是认真的吗？"

    s "我打赌你甚至不知道怎么用多项式计算整数分解。"

    y "啥?"

    scene student happy

    s "我要走了，祝你愉快！"

    scene black with fade

    "..."

    "她显然无法应对我的高智商。"

    jump tutorial_2

label tutorial_2:

    scene black with fade

    "第二天"

    "我走进教室"

    scene student2 smug with fade

    s "Hello"

    t "坐那"

    scene teacher2 grin with fade

    "我坐下"
label tutorial_2_begin:
    scene teacher2 happy

    t "让我们继续上次的话题。"

    t 现在让我们来谈谈提示词，或者一些人所说的听起来就很高大上的“提示工程”。"

    t "写出好的提示对于获得好的图像非常重要。"

    show comfyui prompt_teacher at topleft

    t "下面是一个正面提示的例子。"

    t "这是一个用于生成我的提示符。"

    t "花点时间研究一下。"

    "..."

    t "将单词输入()将改变它们对提示符的影响程度。"

    t "例如(word: 1.2)会增加1.2的效果，而(word: 0.9)会稍微减少效果。"

    t "如果没有为(word)指定权重,那么他就等同于(word:1.1)"

    scene student2 happy with fade

    s "所以我可以用(cute:1.4)来做一些非常可爱的东西"

    scene teacher2 grin with fade

    t "是的，那会把很多Stable Diffusion认为“可爱”的东西放在你的形象中。"

    t "你理解的一个单词的含义和Stable Diffusion所学到的东西可能并不是完全一致的。"

    scene teacher2 happy

    t "此外，1.4的权重可能有点太高，可能会开始造成有问题的形象，所以请记住这一点。"

    scene student2 smug with fade

    s "怎么样..."

    scene student2 blush

    s "如果我采用您的提示并添加(裸体)呢？"

    scene teacher2 blush with fade

    t "求你别这么做。"

    "..."

    scene teacher2 happy

    t "还有一件事。"

    t "您应该尽量使 提示 保持简单。"

    scene teacher2 angry

    t "简单永远是最好的。"

    scene teacher2 happy

    t "如果您在提示中添加太多自相矛盾的术语，您的形象将受到影响。"

    t "Stable Diffusion 无法生成一个符合全部描述词的图像。"

    t "具体提示的效果如何也取决于您使用的检查点(checkpoint)。"

    t "在一个检查点上效果良好的提示可能会在另一个检查点上效果不佳。"

    scene teacher2 grin

    t "这节课就讲到这里，还有问题吗？"

label q3:
    menu:

        "我有个问题"

        "你能重复一遍吗？我没明白。":
            scene teacher2 happy
            t "我会很乐意的。"
            scene black with fade
            jump tutorial_2_begin

        "我爱你":

            jump love_2

        "没关系，我什么都懂。":

            jump understand_2


label love_2:
    scene teacher2 surprised

    t "我受宠若惊。"

    scene teacher2 blush

    t "我也喜欢你，但不是那种喜欢。"

    t "..."

    t "但这只是一个 ComfyUI 教程，请不要转移话题。"
    jump q3

label understand_2:
    scene teacher2 happy

    t "很好，下节课见。"

    "..."

    s "Hey!"

    scene student2 happy

    s "你有空吗？"

label q4:
    menu:

        "我该怎么做?"

        "有.":

            jump go_with_her

        "没空.":

            jump dont_go_with_her


label dont_go_with_her:


    scene student2 crying

    s "我只是想和你做朋友。"

    "..."

    scene black with fade

    "第二天"

    jump tutorial_3

label go_with_her:
    s "耶，我们出去吧。"

    scene student2 angry

    s "我讨厌整天呆在教室里。"

    scene black with fade

    "..."

    scene student_city happy with fade

    s "我喜欢Stable Diffusion。"

    s "我一直不擅长艺术。"

    s "但是现在我可以毫不费力地创作出令人惊叹的艺术作品。"

    y "不过也不是真的没有努力。"

    scene student_city surprised

    y "获得良好的图像可能是困难的, 要做到前后一致真的很麻烦"

    scene student_city grin

    s "你是艺术家吗？"

    s "这项技术完全取代了他们。"

    y "我不这么认为。"

    scene student_city surprised

    y "如果我是一名艺术家，我会将Stable Diffusion集成到我的工作流程中，以使我的流程更有效率。"

    y "艺术家们将非常善于使用Stable Diffusion，因为他们实际上知道是什么使图像看起来还不错。"

    scene student_city angry

    s "那他们为什么这么反对呢？"

    s "他们为什么要抵制它？"

    y "这是新技术，会受到阻碍的。"

    scene student_city surprised

    y "就连使用该技术的人也几乎不知道它实际上是如何运行的时候，所以你不能指望不了解它的人对它有任何了解。"

    y "我把这归咎于“人工智能”这个词。"

    y "Stable Diffusion 没有任何智慧可言。"

    y "在计算机科学中，即使像 Dijkstra 这样的简单算法也可以被称为“人工智能”"

    y "但对于普通人来说，他们认为这就是真正具有智力的东西。"

    y "如果这个名字是“高级应用统计学”，那就没那么可怕了"

    scene student_city blush

    s "所以艺术家们不会因此挨饿吗？"

    y "艺术家们已经在挨饿了。"

    scene student_city crying

    s "可怜的艺术家"

    y "这可能会导致他们中的一些人失业，但也可能为那些费心学习该技术的人开辟新的机会。"

    "..."

    y "好吧，我现在得回家了，和你聊天很开心。"

    scene student_city blush

    s "哦，好的。"

    scene student_city happy

    s "拜拜! 明天见！"

    scene black with fade

    "..."

    "第二天上课前"

    "现在是清晨"

    "我到得很早，所以我去了屋顶"

    scene student_rooftop happy with fade

    "她在这里做什么？"

    y "这么早你在屋顶上干什么？"

    scene student_rooftop surprised

    s "啊，是你！"

    scene student_rooftop happy

    s "我喜欢这里的风景"

    s "还有清晨的新鲜空气。"

    y "我也是......"

    scene student_rooftop grin

    s "我昨晚在玩ComfyUI。"

    scene student_rooftop surprised

    s "它真的可以让你在没有任何过滤器的情况下生成你想要的东西。"

    scene student_rooftop blush

    s "你可以生成任何东西..."

    s "..."

    scene student_rooftop crying

    s "如果有人用它来制作我的照片呢？"

    s "..."

    scene student_rooftop angry

    s "如果有人这样做，我会找到他们，杀了他们。"

    s "所以想都别想。"

    y "没有办法阻止它。"

    scene student_rooftop surprised

    y "有一个“安全过滤器”模型，但它唯一有用的是浪费宝贵的 vram 和处理能力，同时排除掉那些负面的内容"

    y "在我看来，试图让模型"家庭友好"完全是浪费时间。"

    y "这完全取决于用户如何处理他们所获得的工具。"

    y "你不会让一个孩子开车，这是同样的想法。"

    y "即使你滥用了Stable Diffusion你也不能真正的杀死某个人"

    scene student_rooftop grin

    s "所以你同意我生成任何我想要的你的照片吗？"

    y "为..为什么你想要我的照片？"

    scene student_rooftop blush

    s "当我没说。"

    s "好吧，该上课了，我先去。"

    scene black with fade

    "哦，该死，真的该上课了。"

label tutorial_3:

    scene teacher3 grin with fade

    t "欢迎上课"

    scene teacher3 happy

    t "今天我们将讨论负面提示(negative prompt)."

    t "负面提示用于告诉Stable Diffusion您在图像中不想要的东西。"

    show comfyui negative_prompt at topleft

    t "这里有一个负面提示的例子。"

    t "..."

    t "正如你所看到的，它包含了所有我不想在图像中看到的东西。"

    t "其中大多数应该是显而易见的，也许除了(hands)。"

    t "(hands)在负面提示中使用，因为动漫模型创造了太多的手。"

    t "通常人们放(bad hands)，但稳定扩散实际上并不明白什么是“(bad hands)”。"

    t "这就是为什么(hands)同样有效。"

    scene student3 happy

    s "所以，如果我不想要一个糟糕的图像，我可以把（bad image）放在负面提示中？"

    scene teacher3 surprised

    t "不，Stable Diffusion并不能真正理解像什么是坏图像这样的模糊概念。"

    scene teacher3 happy

    t 采样时，负面提示的处理方式与正提示几乎相同。"

    t "该算法采用正提示预测的噪声，并减去用负提示预测的噪声。"

    t "这意味着负面提示对任何可以从图像中减去的东西都非常有效。"

    scene student3 grin

    s "所以我可以把（clothes）放在负面提示里，把它们从图像中删除？"

    scene teacher3 angry

    t "可以，但你为什么要这么做？"

    scene student3 grin

    s "嘿嘿嘿..."

    s "..."

    scene student3 blush

    s "..."

    scene teacher3 angry

    t "我觉得我们应该在课后好好讨论一下你的行为。"

    t "我得把你介绍给我的朋友  安全过滤器。"

    scene student3 crying

    s "不~~~(雪花飘飘~~~)"

    s "除了那个，什么都行！"

    scene teacher3 angry

    t "这是为了你好。"

    scene teacher3 blush

    t "现在我们不要再讨论不合适的事情了。"

    t "..."

    scene teacher3 happy

    t "负面提示和积正面提示一样重要。"

    t "所以一定要用它们做实验。"

    t "有问题吗？"

label q5:
    menu:

        "我有个问题"

        "你能重复一遍吗？我没明白。":
            scene teacher3 happy
            t "当然。"
            scene black with fade
            jump tutorial_3

        "我爱上你了，老师，我们约会吧。":

            jump love_3

        "没关系，我什么都懂。":

            jump understand_3

label love_3:
    scene teacher3 surprised

    t "我对你来说太老了。"

    scene teacher3 blush

    t "我很高兴，但我必须拒绝你。"

    t "..."

    t "这只是一个ComfyUI教程，请保持主题。"
    jump q5

label understand_3:
    scene teacher3 happy

    t "今天就到这里，明天见。"

    "..."

    scene teacher3 grin

    "她指着同学"

    t "当然除了你，你得跟我走。"

    s "呃.."

    scene student3 angry

    "她似乎很生气"

    s "真不敢相信她要把安全过滤器强加给我。"

    scene student3 crying

    s "这是有史以来最糟糕的事情，甚至不能正常工作。"

    y "你活该。"

    scene student3 angry

    s "没有人应该被这样对待，这是不人道的。"

    scene student3 crying

    y "那我们待会儿见吧？"

    y "保重。"

    scene black with fade

    "未完待续"
    return
