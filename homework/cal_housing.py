import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# 准备数据
X, y = fetch_california_housing(return_X_y=True, data_home="./")
x_train, x_val, y_train, y_val = train_test_split(X,y,train_size=0.7)

# 转换为张量
x_train_tensor = torch.as_tensor(x_train, dtype=torch.float32)
y_train_tensor = torch.as_tensor(y_train, dtype=torch.float32).view(-1,1)
x_val_tensor = torch.as_tensor(x_val, dtype=torch.float32)
y_val_tensor = torch.as_tensor(y_val, dtype=torch.float32).view(-1,1)
# Datasets
train_dataset = TensorDataset(x_train_tensor, y_train_tensor)
test_dataset = TensorDataset(x_val_tensor, y_val_tensor)
#Loaders
train_loader = DataLoader(train_dataset, batch_size=400, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=200, shuffle=False)


# 定义模型
class MyLinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(8, 1)
        
    def forward(self, x):
        x = self.fc1(x)
        return x

# mini-batch training
def mini_batch_train(model, train_loader, optimizer, loss_fn):
    mini_batch_losses = []
    for x_batch, y_batch in train_loader:
        model.train()
        # step 1 前向计算预测值
        yhat = model(x_batch)
        # step 2 计算损失
        mini_batch_loss = loss_fn(yhat, y_batch)
        # step 3 反向传播计算梯度
        mini_batch_loss.backward()
        # step 4 更新参数
        optimizer.step()
        # 清空梯度
        optimizer.zero_grad()
        # 记录损失
        mini_batch_losses.append(mini_batch_loss.item())
    
    return np.mean(mini_batch_losses)

# 测试
def mini_batch_val(model, test_loader, optimizer, loss_fn):
    mini_batch_losses = []
    for x_batch, y_batch in test_loader:
        # 置为验证状态
        model.eval()
        # Step 1 - 前向计算预测值
        yhat = model(x_batch)
        # Step 2 - 计算损失
        mini_batch_loss = loss_fn(yhat, y_batch)
        mini_batch_losses.append(mini_batch_loss.item())
    
    return np.mean(mini_batch_losses)

# 训练
def train(model, train_loader, test_loader, optimizer, loss_fn, epochs):
    # 指定随机数种子，可以再现数据
    np.random.seed(23)
    torch.manual_seed(23)

    # 循环轮数计数
    total_epochs = 0
    # 记录训练和验证损失
    train_losses = []
    val_losses = []
    for epoch in range(epochs):
        # 训练
        model.train()
        total_epochs += 1
        train_loss = mini_batch_train(model, train_loader, optimizer, loss_fn)
        train_losses.append(train_loss)
        # 验证
        with torch.no_grad():
            val_loss = mini_batch_val(model, test_loader, optimizer, loss_fn)
            val_losses.append(val_loss)
        
        print(f"Epoch {epoch+1}/{epochs}, train_loss: {train_loss:.4f}, val_loss: {val_loss:.4f}")
    
    return train_losses, val_losses

model = MyLinearRegression()
loss = nn.MSELoss()
lr = 0.001
optimizer = optim.Adam(model.parameters(), lr=lr)
epochs = 500
train_losses, val_losses = train(model, train_loader, test_loader, optimizer, loss, epochs)

# 画图
def plot_losses():
    fig = plt.figure(figsize=(10, 4))
    plt.plot(train_losses, label='Training Loss', c='b')
    plt.plot(val_losses, label='Validation Loss', c='r')
    plt.yscale('log')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.tight_layout()
    return fig

fig=plot_losses()
plt.show()