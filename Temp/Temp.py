# FBXExportAxisConversionMethod [none|convertAnimation|addFbxRoot]; // 轴转化、似乎跟导出轴向上那个有点关系、但没找到
# FBXExportColladaFrameRate [float];  // FBX导出设置中没有找到相关设置、实际上是FBX导出设置中的Collada 的帧速率
# FBXExportColladaSingleMatrix [true|false]; // Collada中的单一矩阵
# FBXExportColladaTriangulate [true|false];  // Collada中的三角化



# 集合体
FBXExportSmoothingGroups -v true|false; // 平滑组
FBXExportHardEdges -v [true|false];   // 逐顶点分割法线
FBXExportTangents -v [true|false]; // 切线和次法线
FBXExportSmoothMesh -v true|false; //平滑网格
# 选择集
FBXExportAnimationOnly -v [true|false]; // 动画、居然是转换为NULL对象
FBXExportInstances -v [true|false]; // 保留实例
FBXExportReferencedAssetsContent -v [true|false]; // 引用的资源内容
FBXExportTriangulate -v [true|false]; // 三角化
# 将NURBS 曲面转化为:NURBS/交互式显示网格/软件渲染网格

# 动画
# 动画

# 附加选项
FBXExportUseSceneName -v [true|false]; // 使用场景名
# 移除单一关键帧 // 当一个物体在时间轴只有一个关键帧的时候、将会被移除
FBXExportQuaternion -v [quaternion|euler|resample]; //四元数插值方式

# 烘焙动画
FBXExportBakeComplexAnimation -v [true|false]; // 烘焙动画
FBXExportBakeComplexStart -v [int]; // 烘焙动画开始帧
FBXExportBakeComplexEnd -v [int]; // 烘焙动画结束帧
FBXExportBakeComplexStep -v [int];// 烘焙动画步长
FBXExportBakeResampleAnimation -v [true|false] // 对动画重采样

# 变形模型
FBXExportShapes -v [true|false]; // 变形模型中的混合模型
FBXExportSkins -v [true|false]; // 变形模型中的蒙皮

# 曲线过滤器
# 曲线过滤器 用于控制开启固定关键帧减少器

# 固定关键帧减少器
FBXExportApplyConstantKeyReducer -v [true|false]; // 固定关键帧减少器
# 平移精度：
# 旋转精度：
# 缩放精度：
# 其他精度：
# 仅自动切线：true or false

# 集合体缓存文件
FBXExportCacheFile -v [true|false]; // 几何体缓存文件
FBXExportQuickSelectSetAsCache –v “setName”; // 集合体缓存文件中的集

# 约束
FBXExportConstraints -v [true|false]; // 约束
FBXExportSkeletonDefinitions -v [true|false]; // 骨架定义

# 摄影机
FBXExportCameras -v [true|false];   // 摄影机

# 灯光
FBXExportLights -v [true|false]; // 灯光

# Audio
FBXExportAudio -v [true|false]; // Audio

# 嵌入的媒体
FBXExportEmbeddedTextures -v [true|false]; // 嵌入的媒体

# 连接
FBXExportIncludeChildren -v [true|false]; // 使用此函数可在导出的 FBX 文件中排除或包含父对象下的层级。 不知道是设置的哪一个（应该是包括子对象）
FBXExportInputConnections -v [true|false]; // 连接（输入连接）





#############
# 高级选项
#############
# 单位
FBXExportConvertUnitString [mm|dm|cm|m|km|In|ft|yd|mi]; // 该命令返回用于将一厘米转化为指定单位所需的比例因子，并且是 FBX 导出器和导入器窗口中“文件单位转化为”菜单的脚本版本。这个是查询转换比例因子
FBXExportScaleFactor [float];	// 比例因子 这个是设置比例因子

# 轴转化
FBXExportUpAxis [y|z]; // 上方向轴

# UI
FBXExportGenerateLog -v [true|false]; // 生成日志数据

# FBX文件格式
FBXExportFileVersion -v [version];  // 导出FBX版本 2018 2019...
FBXExportInAscii -v [true|false]; // 是否导出为ASCII文件

