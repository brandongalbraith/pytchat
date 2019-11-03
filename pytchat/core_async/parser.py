import json
from .. import config
from .. import mylogger
from .. exceptions import ( 
    ResponseContextError, 
    NoContentsException, 
    NoContinuationsException )


logger = mylogger.get_logger(__name__,mode=config.LOGGER_MODE)


class Parser:
    @classmethod
    def parse(cls, jsn):
        if jsn is None: 
            return {'timeoutMs':0,'continuation':None},[]
        if jsn['response']['responseContext'].get('errors'):
            raise ResponseContextError('動画に接続できません。'
        '動画IDが間違っているか、動画が削除／非公開の可能性があります。')
        contents=jsn['response'].get('continuationContents')
        #配信が終了した場合、もしくはチャットデータが取得できない場合
        if contents is None:
            raise NoContentsException('チャットデータを取得できませんでした。')

        cont = contents['liveChatContinuation']['continuations'][0]
        if cont is None:
            raise NoContinuationsException('Continuationがありません。')
        metadata = (cont.get('invalidationContinuationData')  or
                    cont.get('timedContinuationData')         or
                    cont.get('reloadContinuationData')
                    )
        if metadata is None:
            unknown = list(cont.keys())[0]
            if unknown:
                logger.error(f"Received unknown continuation type:{unknown}")
                metadata = cont.get(unknown)
        metadata.setdefault('timeoutMs', 10000)
        chatdata = contents['liveChatContinuation'].get('actions')
        return metadata, chatdata