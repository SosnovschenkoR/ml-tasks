import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


async def main():
    await asyncio.gather(tick(), tick(), tick())
    for taks in asyncio.all_tasks():
        print(taks, end='\n')


if __name__ == '__main__':
    coroutine = main()
    # print(coroutine)
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        # loop.create_task(main())
        # loop.run_forever()
        print('coroutine has finshed')
    except KeyboardInterrupt:
        print('Manually closed')
    finally:
        loop.close()
        print('loop is closed')
