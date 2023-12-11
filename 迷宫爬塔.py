import pygame
import random

def dfs(po):
    m[po[0]][po[1]] = ' '
    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(di)
    for d in di:
        next = (po[0]+d[0]*2, po[1]+d[1]*2)
        if 0 <= next[0] < H and 0 <= next[1] < W and m[next[0]][next[1]] == '#':
            m[po[0]+d[0]][po[1]+d[1]] = ' '
            dfs(next)


# 设置迷宫大小
W = int(input('请输入迷宫的长度: '))
H = int(input('请输入迷宫的宽度: '))

# 创建迷宫数据
m = [['#' for _ in range(W)] for _ in range(H)]
start = (0, 0)
end = (H - 1, W - 1)
dfs(start)
m[H-1][W-1]=' '
m[H-1][W-2]=' '

# 初始化pygame
pygame.init()

# 设置窗口大小
cell_size = 40
screen_width = W * cell_size
screen_height = H * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption('迷宫')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 方块的初始位置
block_x, block_y = start

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and block_y > 0 and m[block_y - 1][block_x] == ' ':
                block_y -= 1
            elif event.key == pygame.K_DOWN and block_y < H - 1 and m[block_y + 1][block_x] == ' ':
                block_y += 1
            elif event.key == pygame.K_LEFT and block_x > 0 and m[block_y][block_x - 1] == ' ':
                block_x -= 1
            elif event.key == pygame.K_RIGHT and block_x < W - 1 and m[block_y][block_x + 1] == ' ':
                block_x += 1

            # 检查是否到达终点
            if (block_y, block_x) == end:
                # 重置迷宫和方块位置
                m = [['#' for _ in range(W)] for _ in range(H)]
                dfs(start)
                block_x, block_y = start

    # 填充背景色
    screen.fill(WHITE)

    # 绘制迷宫
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size))

    # 绘制终点
    pygame.draw.rect(screen, GREEN, (end[1] * cell_size, end[0] * cell_size, cell_size, cell_size))

    # 绘制可控制的方块
    pygame.draw.rect(screen, BLUE, (block_x * cell_size, block_y * cell_size, cell_size, cell_size))

    # 更新屏幕显示
    pygame.display.flip()

# 退出游戏
pygame.quit()