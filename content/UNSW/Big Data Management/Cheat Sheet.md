### Question 1
(a) (2 marks) Explain the data flow in MapReduce using the word count problem as an example.
1. The mapper read the data from HDFS. A mapper task is started for each HDFS data block. Each record is processed by one map function. The mapper output is sorted and stored on local disks. 
2. In order to reduce the mapper output size and save the network I/O cost, a combiner can be designed to perform local aggregation. 
3. According to the number of reducers specified, the mapper output is partitioned to several groups, each corresponding to one reducer. 
4. The reducer fetches its partition from each mapper and merges the locally sorted data to obtain a global order. Next, each key and its associated values are processed by one reducer function. The output is stored back to HDFS.
(b) (2 marks) Explain the data flow in Spark using the word count problem as an example. 
5. RDD/DataFrame operations are categorized into transformation and action, and the transformation operations are lazily evaluated. 
6. When reaching an action, a job will be created, and the real execution begins at this point.
7. Each transformation operation that requires data shuffling becomes the boundary of stages. Spark create a DAG based on the stages. 
8. Within each stage, a task will be run for each partition on an executor, and the tasks run in parallel.
(a) (2 marks) Show four differences between MapReduce and Spark.
- **Storage:** MapReduce on disk, Spark in memory.
- **Model:** MapReduce = 2-stage, Spark = DAG.
- **Latency:** MapReduce high, Spark low.
- **API:** MapReduce Java-only, Spark multi-language + rich APIs.
#### **Combiner in Project 1**
1. **Why combiner helps performance?**
    - It reduces the amount of intermediate data transferred across the network (local aggregation), lowering shuffle cost.
2. **External vs In-mapper combiner**
    - **External combiner** (the Hadoop framework’s combiner function):
        - _Advantage_: Easy to use, integrated into Hadoop.
        - _Disadvantage_: Execution not guaranteed, may run 0 or multiple times.
    - **In-mapper combiner** (using local data structure inside mapper):
        - _Advantage_: Full control, guaranteed aggregation, fewer intermediate pairs.
        - _Disadvantage_: More code complexity, higher memory usage inside mapper.
#### **Order inversion & value-to-key pattern in Project 1**
1. **Order inversion**: Emit a special key to ensure global statistics (e.g., marginal counts) are processed first → avoids storing all data in memory.
2. **Value-to-key conversion**: Move values to the key to allow grouping & sorting by Hadoop’s shuffle → reduces reducer workload.
3. Both improve performance by **reducing memory usage** and **exploiting shuffle sorting** instead of manual handling.
#### **Stopwords filtering in Project 2**
- **Data structure**: Use a **HashSet** (fast O(1) membership check, no duplicates).
- **Spark feature**: **Broadcast variable** (each worker gets a local copy without repeated shipping).
- **Reason**: Efficient lookup + avoids expensive repeated data transfer.
#### **Fault tolerance in Spark (Project 2)**
- **Spark fault tolerance**: Uses **RDD lineage (DAG)**; lost partitions can be recomputed from original transformations.
- **MapReduce fault tolerance**: Relies on **replication and task re-execution**; intermediate data is written to disk, tasks rerun if failed.
- **Difference**: Spark recomputes lost data from lineage (in-memory, faster); MapReduce reloads from disk copies (slower, more I/O).
#### What is the best data structure to store the high-frequency words when broadcasting them?
Set. In Python, the search complexity using a set (expected to be O(1)) is better than that of using a list or an array (log(N)).
#### Project 3: why writing to disk is slow
Transformations such as `map()`, `flatMap()`, and `filter()` are lazy, so they only build the DAG. The actual computation is triggered when the final action (`saveAsTextFile()`) is called, and writing to disk is inherently expensive. This is why most of the time is spent at the last step.
### Question 2
![[Pasted image 20250821191539.png]]
- **Mapper:** for each record, Emit(department + “,” + salary, name) 
- **Combiner:** find out all persons with the local maximum salary for each department 
- **Reducer:** receives data ordered by (department, salary), the first one is the maximum salary in a department. Check the next one until reaching a smaller salary and ignore all remaining. Save all persons with this maximum salary in the department 
- **JOBCONF:** key partitioned by “-k1,1”, sorted by “-k1,1 -k2,2nr”
![[Pasted image 20250822191832.png]]
```Python
class Question1 
	method map(self, userID, list of locations) 
		for each loc in the list of locations 
			Emit("loc, userID", "") 
	method reduce_init(self) 
		current_loc = "" current_list = [] 
	method reduce(self, key, value) 
		loc, userID = key.split(",") 
		if loc != current_loc 
			if current_loc!=“” 
				Emit(current_loc, current_list) 
			current_list = [] 
			current_list.add(userID) 
			current_loc=loc 
		else 
			current_list.add(userID) 
	method reduce_final(self) 
		Emit(current_loc, current_list) 
In JOBCONF, configure: 
	'mapreduce.map.output.key.field.separator':’,’, 
	'mapreduce.partition.keypartitioner.options':'-k1,1’, 
	'mapreduce.partition.keycomparator.options':'-k1,1 -k2,2'
```
![[Pasted image 20250822191609.png]]
- **Mapper**:  
    For each complete sentence (split by “`.` ”), tokenize by space, remove duplicates within the sentence, generate all unordered pairs of distinct terms. For each pair `(u, w)`, enforce alphabetical order inside the pair `(min(u,w), max(u,w))`.  
    Emit(pair, 1).
- **Combiner**:  
    For each pair, sum local counts to reduce network I/O.
- **Reducer**:  
    Receives data ordered by (−count, pair). The reducer outputs the first _k_ records:
    - The ordering ensures frequency descending, with ties broken by alphabetical order of pair.
    - Emit(pair, total_count) until _k_ outputs are reached.
- **JOBCONF**:  
    Key partitioned by “`-k1,1`”, sorted by “`-k1,1 -k2,2`”.
    - Field separator: “, ”
    - Reducer number: 1 (for global top-k)
![[Pasted image 20250822192816.png|800]]
### Question 3
![[Pasted image 20250821200347.png]]
```Python
// 1) (term, docId) 去重（同一文档内出现多次也只算一次）
val termDoc: RDD[(String, Int)] =
  docs.flatMap { case (docId, text) =>
        text.toLowerCase.split("\\W+").filter(_.nonEmpty).distinct
            .map(term => (term, docId))
      }
// 2) 聚合成倒排表，并把 docId 升序
val invList: RDD[(String, List[Int])] =
  termDoc.groupByKey()
         .mapValues(ids => ids.toSet.toList.sorted)
// 3) term 按字母序升序
val InvList = invList.sortByKey(ascending = true)
```
![[Pasted image 20250821200405.png]]
```Python
val df = pairs.toDF("key", "value")
// 统计每个 key 的最小值、最大值并求 gap，过滤后按 key 降序
val resMinMax =
  df.groupBy($"key")
    .agg(min($"value").as("minv"), max($"value").as("maxv"))
    .withColumn("gap", $"maxv" - $"minv")
    .filter($"gap" > 100)
    .select($"key")                // 只要 key；若想带上 min/max/gap 可保留这些列
    .orderBy(desc("key"))
```
### Question 4 Mining Data Streams
![[Pasted image 20250821212508.png|475]] ![[Pasted image 20250821213559.png|675]]
### Question 5 Finding Similar Items
![[Pasted image 20250822172227.png|625]]
Locality-Sensitive Hashing
![[Pasted image 20250822185713.png|500]]
### Question 6
![[Pasted image 20250821224947.png|475]]