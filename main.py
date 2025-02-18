from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event import MessageChain

@register("helloworld", "Your Name", "一个简单的 Hello World 插件", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("opl")
    async def opl(self, event: AstrMessageEvent):
        '''这是一个 hello world 指令''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        umo = event.unified_msg_origin
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = MessageChain().message(message_str)
        logger.info(message_chain)
        s=event.get_group_id()
        if event.get_platform_name() == "aiocqhttp":
        # qq
            from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import AiocqhttpMessageEvent
            assert isinstance(event, AiocqhttpMessageEvent)
            client = event.bot # 得到 client
            payloads = {
                "group_id": "1031311599",
                "nessage":[
                    {
                        "type": "text",
                        "data": {
                            "text": "napcat"
                        }
                    }
                ]
            }
            ret = await client.api.call_action('', **payloads) # 调用 协议端  API
            logger.info(f"delete_msg: {ret}")
        yield event.plain_result(f"消息已转发{s}") # 发送一条纯文本消息