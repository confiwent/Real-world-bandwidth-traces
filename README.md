# Real-world-bandwidth-traces
Real-world network throughputs traces used in MERINA(+) [\[paper\]](https://dl.acm.org/doi/abs/10.1145/3503161.3548331).

> Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong. 2022. Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning. In Proceedings of the 30th ACM International Conference on Multimedia (MM '22). Association for Computing Machinery, New York, NY, USA, 3006–3016. https://doi.org/10.1145/3503161.3548331

A collection of four public real-world network throughput datasets for simulating various user and network conditions. All traces are pre-processed with the format of `[time_stamp (sec), throughput (Mbit/sec)]`. Refer to [Pensieve](https://github.com/confiwent/pensieve/tree/master/traces) for more details.

- _3G/HSDPA_ dataset, published in [Commute Path Bandwidth Traces from 3G Networks](https://qualinet.github.io/databases/commute_path_bandwidth_traces_from_3g_networks/), which is stored in `./cooked_3gp/` and `./traces_3gp`. 

- _FCC_ dataset, collected from [Raw Data-Measuring Broadband
America. (2016)](https://www.fcc.gov/reports-research/reports/measuring-broadband-america/raw-data-measuring-broadband-america-2016), which is stored in `./fcc_ori/`.

- _FCC & HSDPA_ dataset, which includes mixed traces from FCC and 3G/HSDPA and is stored in `./fcc_and_hsdpa/`.

- _Oboe_ dataset, published in [Oboe: auto-tuning video ABR algorithms to network conditions](https://dl.acm.org/doi/10.1145/3230543.3230558), which is stored in `./traces_oboe/`.

- _Puffer_ dataset, collected from [Puffer platform](https://puffer.stanford.edu/). We precess all traces on two randomly chosen dates (Oct. 17, 2021 and Feb.
18, 2022), and the results are stored in `./puffer_211017/` and `./puffer_220218/`, respectively.

- `./load_webget_data.py` shows how to process raw Puffer traces. 
