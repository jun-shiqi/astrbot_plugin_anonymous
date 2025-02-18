from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event import MessageChain

@register("nonymous", "junshiqi", "这是一个匿名传话的小插件", "1.0.0", "https://github.com/jun-shiqi/astrbot_plugin_anonymous")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("匿名")
    async def nonymous(self, event: AstrMessageEvent):
        '''这是一个匿名传话的小插件''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        if event.get_platform_name() == "aiocqhttp":
            from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import AiocqhttpMessageEvent
            assert isinstance(event, AiocqhttpMessageEvent)
            client = event.bot # 得到 client
            massage_list=event.message_str.split(" ")
            g_id=massage_list[1]
            massage=massage_list[2]
            payloads = {
                "group_id": g_id,
                "message": [
                    {
                        "type": "text",
                        "data": {
                        "text": massage
                        }
                    }
                ]
            }
            ret = await client.api.call_action('send_group_msg', **payloads) # 调用 协议端  API
            logger.info(f"delete_msg: {ret}")
            yield event.plain_result(f"消息已转发") # 发送一条纯文本消息
    
    
    @filter.command("匿名帮助")
    async def help(self,event:AstrMessageEvent):
        yield event.plain_result(f"使用该功能小窗机器人可以实现匿名传话。格式为/匿名 qq群号 内容") # 发送一条纯文本消息
    