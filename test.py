"""
BMI计算器 - 图形界面版本
根据BMI公式（体重除以身高的平方）计算BMI指数并提供健康建议

功能特色：
- 智能BMI计算和分类
- 个性化的健康建议
- 详细的饮食和运动指导
- 完整的健康建议指南

使用说明：
- 身高请输入厘米（cm）
- 体重请输入公斤（kg）
- 点击"健康建议"查看详细指导

BMI标准：
 低于18.5：过轻
 18.5-25：正常
 25-28：过重
 28-32：肥胖
 高于32：严重肥胖
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math


class BMICalculator:
    """BMI计算器GUI类"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI健康计算器")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # 设置样式
        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('微软雅黑', 16, 'bold'))
        self.style.configure('Custom.TButton', font=('微软雅黑', 10))

        self.setup_ui()
        self.center_window()

    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="BMI 健康计算器",
            style='Title.TLabel'
        )
        title_label.pack(pady=(0, 20))

        # 输入框架
        input_frame = ttk.LabelFrame(main_frame, text="请输入您的信息", padding="15")
        input_frame.pack(fill=tk.X, pady=(0, 20))

        # 身高输入
        height_frame = ttk.Frame(input_frame)
        height_frame.pack(fill=tk.X, pady=(0, 10))

        height_label = ttk.Label(height_frame, text="身高 (cm):", width=10)
        height_label.pack(side=tk.LEFT)

        self.height_var = tk.StringVar()
        height_entry = ttk.Entry(
            height_frame,
            textvariable=self.height_var,
            font=('微软雅黑', 10)
        )
        height_entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

        # 体重输入
        weight_frame = ttk.Frame(input_frame)
        weight_frame.pack(fill=tk.X, pady=(0, 20))

        weight_label = ttk.Label(weight_frame, text="体重 (kg):", width=10)
        weight_label.pack(side=tk.LEFT)

        self.weight_var = tk.StringVar()
        weight_entry = ttk.Entry(
            weight_frame,
            textvariable=self.weight_var,
            font=('微软雅黑', 10)
        )
        weight_entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

        # 按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20))

        # 创建内部框架用于居中按钮
        button_inner_frame = ttk.Frame(button_frame)
        button_inner_frame.pack(expand=True)

        # 计算按钮
        calculate_btn = ttk.Button(
            button_inner_frame,
            text="计算BMI",
            command=self.calculate_bmi,
            style='Custom.TButton'
        )
        calculate_btn.pack(side=tk.LEFT, padx=(0, 10))

        # 清空按钮
        clear_btn = ttk.Button(
            button_inner_frame,
            text="清空",
            command=self.clear_inputs,
            style='Custom.TButton'
        )
        clear_btn.pack(side=tk.LEFT, padx=(10, 0))

        # 健康建议按钮
        suggestion_btn = ttk.Button(
            button_inner_frame,
            text="健康建议",
            command=self.show_health_suggestions,
            style='Custom.TButton'
        )
        suggestion_btn.pack(side=tk.LEFT, padx=(10, 0))

        # 结果框架
        result_frame = ttk.LabelFrame(main_frame, text="计算结果", padding="15")
        result_frame.pack(fill=tk.X)

        # BMI结果
        self.bmi_var = tk.StringVar()
        self.bmi_var.set("BMI指数: --")
        bmi_label = ttk.Label(
            result_frame,
            textvariable=self.bmi_var,
            font=('微软雅黑', 12, 'bold')
        )
        bmi_label.pack(anchor=tk.W, pady=(0, 5))

        # 健康建议
        self.result_var = tk.StringVar()
        self.result_var.set("健康建议: 请先输入身高和体重")
        result_label = ttk.Label(
            result_frame,
            textvariable=self.result_var,
            font=('微软雅黑', 10)
        )
        result_label.pack(anchor=tk.W)

        # 绑定回车键
        self.root.bind('<Return>', lambda e: self.calculate_bmi())
        self.root.bind('<Escape>', lambda e: self.clear_inputs())

    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"+{x}+{y}")

    def calculate_bmi(self):
        """计算BMI指数"""
        try:
            height_cm = float(self.height_var.get())
            weight = float(self.weight_var.get())

            if height_cm <= 0 or weight <= 0:
                messagebox.showerror("输入错误", "身高和体重必须大于0")
                return

            # 将厘米转换为米
            height = height_cm / 100

            if height > 3:
                messagebox.showwarning("输入提示", "身高是否超过300厘米？请检查输入")

            bmi = weight / (height ** 2)

            # 更新BMI显示
            self.bmi_var.set(f"BMI指数: {bmi:.2f}")
            # 获取健康建议
            result_text = self.get_bmi_result(bmi)
            self.result_var.set(f"健康建议: {result_text}")

            # 显示详细信息
            self.show_detailed_info(bmi, height, weight)

        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字")
        except Exception as e:
            messagebox.showerror("计算错误", f"发生未知错误: {str(e)}")

    def get_bmi_result(self, bmi):
        """根据BMI值获取健康建议"""
        if bmi < 18.5:
            return "您体质过轻，建议增加营养摄入，均衡饮食，加强身体锻炼"
        elif 18.5 <= bmi < 25:
            return "您体质正常，继续保持健康生活方式，定期体检"
        elif 25 <= bmi < 28:
            return "您体质过重，建议适当控制饮食，增加运动量，建立健康生活习惯"
        elif 28 <= bmi < 32:
            return "您体质肥胖，建议咨询医生或营养师，制定科学的减重计划"
        else:
            return "您严重肥胖，建议立即咨询医生，接受专业医疗指导"

    def get_detailed_suggestions(self, bmi):
        """获取详细的健康建议"""
        if bmi < 18.5:
            return """
【饮食建议】
• 增加每日热量摄入300-500卡路里
• 多摄入优质蛋白质：鱼类、瘦肉、蛋类、豆类
• 增加碳水化合物：全谷类、薯类
• 适量增加健康脂肪：坚果、橄榄油、鳄梨

【运动建议】
• 进行力量训练：增加肌肉质量
• 每周3-4次阻力训练
• 结合有氧运动：快走、游泳、骑自行车

【生活建议】
• 保证充足睡眠：每日7-9小时
• 规律三餐，避免暴饮暴食
• 必要时咨询营养师"""

        elif 18.5 <= bmi < 25:
            return """
【饮食建议】
• 保持均衡饮食：多样化食物选择
• 控制总热量摄入，维持理想体重
• 增加蔬果摄入：每日500g以上
• 适量摄入优质蛋白和健康脂肪

【运动建议】
• 保持中等强度运动：每周150分钟
• 结合有氧和力量训练
• 养成日常活动习惯：多走楼梯、散步

【生活建议】
• 定期体检：每年1次全面检查
• 保持健康生活方式
• 管理压力，保持心理健康"""

        elif 25 <= bmi < 28:
            return """
【饮食建议】
• 控制总热量摄入：每日减少300-500卡路里
• 减少精制碳水化合物和糖分摄入
• 增加膳食纤维：多吃蔬果和全谷类
• 采用少食多餐模式，避免饥饿感

【运动建议】
• 增加有氧运动：每周200-300分钟中等强度
• 结合高强度间歇训练（HIIT）
• 增加日常活动：步行、骑车代替开车

【生活建议】
• 记录饮食日记，监控摄入量
• 建立支持系统，寻求家人朋友帮助
• 定期监测体重变化"""

        elif 28 <= bmi < 32:
            return """
【饮食建议】
• 咨询营养师制定个性化饮食计划
• 严格控制热量摄入，科学减重
• 增加高纤维、低热量食物
• 避免高糖、高脂食物

【运动建议】
• 在医生指导下进行运动
• 选择低冲击性运动：游泳、水中健身
• 结合力量训练和心肺功能训练
• 建议寻求专业教练指导

【生活建议】
• 必须咨询医疗专业人士
• 定期监测相关健康指标
• 考虑行为疗法改变生活习惯"""

        else:
            return """
【饮食建议】
• 立即咨询医生或营养师
• 制定严格的医疗监督减重计划
• 可能需要特殊饮食干预
• 避免自行极端节食

【运动建议】
• 必须在医生监督下进行
• 从低强度活动开始，逐渐增加
• 可能需要康复训练
• 避免高强度运动风险

【生活建议】
• 寻求专业医疗帮助
• 进行全面健康评估
• 考虑心理支持和咨询
• 制定长期健康管理计划"""

    def show_detailed_info(self, bmi, height, weight):
        """显示详细信息"""
        height_cm = height * 100  # 转换回厘米显示
        suggestions = self.get_detailed_suggestions(bmi)

        info = f"""
BMI指数: {bmi:.2f}

身高: {height_cm:.0f} cm
体重: {weight:.1f} kg

健康状态: {self.get_bmi_result(bmi)}

详细建议:{suggestions}
"""
        messagebox.showinfo("BMI详细信息", info)

    def show_health_suggestions(self):
        """显示健康建议窗口"""
        suggestion_window = tk.Toplevel(self.root)
        suggestion_window.title("BMI健康建议")
        suggestion_window.geometry("600x500")
        suggestion_window.resizable(False, False)

        # 创建主框架
        main_frame = ttk.Frame(suggestion_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="BMI 健康建议指南",
            font=('微软雅黑', 14, 'bold')
        )
        title_label.pack(pady=(0, 20))

        # 创建文本区域
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 文本显示区域
        text_widget = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=('微软雅黑', 10),
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=text_widget.yview)

        # 插入健康建议内容
        suggestions_text = """
BMI健康建议详细指南

1. 体质过轻 (BMI < 18.5)
【饮食建议】
• 增加每日热量摄入300-500卡路里
• 多摄入优质蛋白质：鱼类、瘦肉、蛋类、豆类
• 增加碳水化合物：全谷类、薯类
• 适量增加健康脂肪：坚果、橄榄油、鳄梨

【运动建议】
• 进行力量训练：增加肌肉质量
• 每周3-4次阻力训练
• 结合有氧运动：快走、游泳、骑自行车

【生活建议】
• 保证充足睡眠：每日7-9小时
• 规律三餐，避免暴饮暴食
• 必要时咨询营养师

2. 体质正常 (18.5 ≤ BMI < 25)
【饮食建议】
• 保持均衡饮食：多样化食物选择
• 控制总热量摄入，维持理想体重
• 增加蔬果摄入：每日500g以上
• 适量摄入优质蛋白和健康脂肪

【运动建议】
• 保持中等强度运动：每周150分钟
• 结合有氧和力量训练
• 养成日常活动习惯：多走楼梯、散步

【生活建议】
• 定期体检：每年1次全面检查
• 保持健康生活方式
• 管理压力，保持心理健康

3. 体质过重 (25 ≤ BMI < 28)
【饮食建议】
• 控制总热量摄入：每日减少300-500卡路里
• 减少精制碳水化合物和糖分摄入
• 增加膳食纤维：多吃蔬果和全谷类
• 采用少食多餐模式，避免饥饿感

【运动建议】
• 增加有氧运动：每周200-300分钟中等强度
• 结合高强度间歇训练（HIIT）
• 增加日常活动：步行、骑车代替开车

【生活建议】
• 记录饮食日记，监控摄入量
• 建立支持系统，寻求家人朋友帮助
• 定期监测体重变化

4. 肥胖 (28 ≤ BMI < 32)
【饮食建议】
• 咨询营养师制定个性化饮食计划
• 严格控制热量摄入，科学减重
• 增加高纤维、低热量食物
• 避免高糖、高脂食物

【运动建议】
• 在医生指导下进行运动
• 选择低冲击性运动：游泳、水中健身
• 结合力量训练和心肺功能训练
• 建议寻求专业教练指导

【生活建议】
• 必须咨询医疗专业人士
• 定期监测相关健康指标
• 考虑行为疗法改变生活习惯

5. 严重肥胖 (BMI ≥ 32)
【饮食建议】
• 立即咨询医生或营养师
• 制定严格的医疗监督减重计划
• 可能需要特殊饮食干预
• 避免自行极端节食

【运动建议】
• 必须在医生监督下进行
• 从低强度活动开始，逐渐增加
• 可能需要康复训练
• 避免高强度运动风险

【生活建议】
• 寻求专业医疗帮助
• 进行全面健康评估
• 考虑心理支持和咨询
• 制定长期健康管理计划

温馨提示：
• 以上建议仅供参考
• 具体情况请咨询专业医师
• 保持积极心态，坚持健康生活方式
"""

        text_widget.insert(tk.END, suggestions_text)
        text_widget.config(state=tk.DISABLED)  # 设置为只读

        # 关闭按钮
        close_btn = ttk.Button(
            main_frame,
            text="关闭",
            command=suggestion_window.destroy
        )
        close_btn.pack(pady=(20, 0))

        # 让窗口居中
        suggestion_window.transient(self.root)
        suggestion_window.grab_set()
        self.root.wait_window(suggestion_window)

    def clear_inputs(self):
        """清空输入"""
        self.height_var.set("")
        self.weight_var.set("")
        self.bmi_var.set("BMI指数: --")
        self.result_var.set("健康建议: 请先输入身高和体重")

    def run(self):
        """运行程序"""
        self.root.mainloop()


def main():
    """主函数"""
    try:
        app = BMICalculator()
        app.run()
    except Exception as e:
        print(f"程序启动失败: {str(e)}")
        # 如果GUI无法启动，尝试命令行版本
        print("\nGUI版本启动失败，尝试命令行版本...")
        try:
            height_cm = float(input("请输入您的身高(cm): "))
            weight = float(input("请输入您的体重(kg): "))
            height = height_cm / 100  # 转换为米
            bmi = weight / (height ** 2)
            print(f"您的BMI指数为: {bmi:.2f}")
            if bmi < 18.5:
                print("您体质过轻")
            elif 18.5 <= bmi < 25:
                print("您体质正常")
            elif 25 <= bmi < 28:
                print("您体质过重")
            elif 28 <= bmi < 32:
                print("您体质肥胖")
            else:
                print("您严重肥胖")
            bmi = weight / (height ** 2)
            print(f"您的BMI指数为: {bmi:.2f}")
            if bmi < 18.5:
                print("您体质过轻")
            elif 18.5 <= bmi < 25:
                print("您体质正常")
            elif 25 <= bmi < 28:
                print("您体质过重")
            elif 28 <= bmi < 32:
                print("您体质肥胖")
            else:
                print("您严重肥胖")
        except Exception as e2:
            print(f"命令行版本也失败了: {str(e2)}")


if __name__ == "__main__":
    main()



