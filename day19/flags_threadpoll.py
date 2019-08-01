# from concurrent import futures
#
# from day19.Http_Request import save_flag, get_flag, show, main
#
# MAX_WORKERS = 20
#
# def download_one(game):
#     image = get_flag(game)
#     show(game)
#     save_flag(image, game + '.jpg')
#     return game
#
# def download_many(game_list):
#     workers = min(MAX_WORKERS, len(game_list))
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, sorted(game_list))
#
#     return len(list(res))
from concurrent import futures
from Http_Request import save_flag, get_flag, show, main

MAX_WORKERS = 20
def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ProcessPoolExecutor() as executor:
        # res = executor.map(download_one, sorted(cc_list))
        todo = []
        for  cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            todo.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))
        # import time
        # # print('sleep..')
        # # time.sleep(0.5)
        # # print('sleep down')
        results = []
        for future in futures.as_completed(todo):
            res = future.result()
            msg = '{} result {!r}'
            print(msg.format(future, res))

    return len(results)


if __name__ == '__main__':
    main(download_many)


# if __name__ == '__main__':
#     main(download_many)


