import asyncio
from preloaded import send_request


async def request_manager(n: int) -> str:
    #Ограничение запросов
    semaphore = asyncio.Semaphore(150)
    
    async def make_request():
        async with semaphore: # Ожидаем свободного слота
            return await send_request()
    
    
    # Создаем и запускаем все задачи сразу
    tasks = [make_request() for _ in range(n)]
    
    # Ждем завершения ВСЕХ задач параллельно
    results = await asyncio.gather(*tasks)
    
    return ''.join(results)
