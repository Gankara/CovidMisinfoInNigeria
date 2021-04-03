import pandas as pd
import os

res_a = pd.read_csv('data/tsv/a2_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_a = pd.DataFrame(['Covid'] * len(res_a.index), columns=['37'])
res1 = pd.concat([res_a, tweets_a], axis=1)

res_b = pd.read_csv('data/tsv/b.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_b = pd.DataFrame(['CovidNigeria'] * len(res_b.index), columns=['37'])
res2 = pd.concat([res_b, tweets_b], axis=1)

res_c = pd.read_csv('data/tsv/c2_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_c = pd.DataFrame(['Covid-19'] * len(res_c.index), columns=['37'])
res3 = pd.concat([res_c, tweets_c], axis=1)

res_d = pd.read_csv('data/tsv/d.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_d = pd.DataFrame(['Covid19Lagos'] * len(res_d.index), columns=['37'])
res4 = pd.concat([res_d, tweets_d], axis=1)

res_e = pd.read_csv('data/tsv/e.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_e = pd.DataFrame(['CovidLagos'] * len(res_e.index), columns=['37'])
res5 = pd.concat([res_e, tweets_e], axis=1)

res_f = pd.read_csv('data/tsv/f1_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_f = pd.DataFrame(['Covid19'] * len(res_f.index), columns=['37'])
res6 = pd.concat([res_f, tweets_f], axis=1)

res_g = pd.read_csv('data/tsv/g_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_g = pd.DataFrame(['Covid19Updates'] * len(res_g.index), columns=['37'])
res7 = pd.concat([res_g, tweets_g], axis=1)

res_h = pd.read_csv('data/tsv/h_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_h = pd.DataFrame(['Covid19Pandemic'] * len(res_h.index), columns=['37'])
res8 = pd.concat([res_h, tweets_h], axis=1)

res_i = pd.read_csv('data/tsv/i_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_i = pd.DataFrame(['Covik19'] * len(res_i.index), columns=['37'])
res9 = pd.concat([res_i, tweets_i], axis=1)


res_j = pd.read_csv('data/tsv/j.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_j = pd.DataFrame(['CoronaNigeria'] * len(res_j.index), columns=['37'])
res10 = pd.concat([res_j, tweets_j], axis=1)

res_k = pd.read_csv('data/tsv/k.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_k = pd.DataFrame(['CoronaVirusInNigeria'] * len(res_k.index), columns=['37'])
res11 = pd.concat([res_k, tweets_k], axis=1)

res_l = pd.read_csv('data/tsv/l.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_l = pd.DataFrame(['CoronaVirusNigeria'] * len(res_l.index), columns=['37'])
res12 = pd.concat([res_l, tweets_l], axis=1)

res_m = pd.read_csv('data/tsv/m_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_m = pd.DataFrame(['CoronaUpdate'] * len(res_m.index), columns=['37'])
res13 = pd.concat([res_m, tweets_m], axis=1)

res_n = pd.read_csv('data/tsv/n_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_n = pd.DataFrame(['CoronaOutbreak'] * len(res_n.index), columns=['37'])
res14 = pd.concat([res_n, tweets_n], axis=1)

res_o = pd.read_csv('data/tsv/o.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_o = pd.DataFrame(['StaysafeNigeria, StaysafeNaija'] * len(res_o.index), columns=['37'])
res15 = pd.concat([res_o, tweets_o], axis=1)

res_p = pd.read_csv('data/tsv/p.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_p = pd.DataFrame(['StaysafeNigeria,StaysafeNaija'] * len(res_p.index), columns=['37'])
res16 = pd.concat([res_p, tweets_p], axis=1)

res_q = pd.read_csv('data/tsv/q_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_q = pd.DataFrame(['StayAtHome'] * len(res_q.index), columns=['37'])
res17 = pd.concat([res_q, tweets_q], axis=1)

res_r = pd.read_csv('data/tsv/r_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_r = pd.DataFrame(['MaskUp'] * len(res_r.index), columns=['37'])
res18 = pd.concat([res_r, tweets_r], axis=1)

res_s = pd.read_csv('data/tsv/s.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_s = pd.DataFrame(['MaskUpLagos, MaskUpNigeria'] * len(res_s.index), columns=['37'])
res19 = pd.concat([res_s, tweets_s], axis=1)

res_u = pd.read_csv('data/tsv/u1_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_u = pd.DataFrame(['NCDC'] * len(res_u.index), columns=['37'])
res20 = pd.concat([res_u, tweets_u], axis=1)

res_v = pd.read_csv('data/tsv/v.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_v = pd.DataFrame(['NCDCgovNigeria, NCDCNigeria'] * len(res_v.index), columns=['37'])
res21 = pd.concat([res_v, tweets_v], axis=1)

res_w = pd.read_csv('data/tsv/w1_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_w = pd.DataFrame(['NCDCgov, NCDCTakeResponsibility'] * len(res_w.index), columns=['37'])
res22 = pd.concat([res_w, tweets_w], axis=1)

res_x = pd.read_csv('data/tsv/x.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_x = pd.DataFrame(['NoLockdownLagos'] * len(res_x.index), columns=['37'])
res23 = pd.concat([res_x, tweets_x], axis=1)

res_y = pd.read_csv('data/tsv/y.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_y = pd.DataFrame(['LockdownLagos'] * len(res_y.index), columns=['37'])
res24 = pd.concat([res_y, tweets_y], axis=1)

res_z = pd.read_csv('data/tsv/z_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_z = pd.DataFrame(['LockdownExtension'] * len(res_z.index), columns=['37'])
res25 = pd.concat([res_z, tweets_z], axis=1)

res_aa = pd.read_csv('data/tsv/aa_ng.tsv', sep='\t', error_bad_lines=False, header=None)
tweets_aa = pd.DataFrame(['Lockdown'] * len(res_aa.index), columns=['37'])
res26 = pd.concat([res_aa, tweets_aa], axis=1)


frames = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13, res14,
          res15, res16, res17, res18, res19, res20, res21, res22, res23, res24, res25, res26]
res = pd.concat(frames)

res.columns = ['tweet_created_at',
               'tweet_id',
               'tweet_text',
               'tweet_truncated',
               'tweet_source',
               'tweet_in_reply_to_status_id',
               'tweet_in_reply_to_user_id',
               'tweet_in_reply_to_screen_name',
               'tweet_coordinates',
               'tweet_place',
               'tweet_user',
               'tweet_full_text',
               'tweet_entities',
               'tweet_lang',
               'tweet_is_quote_status',
               'tweet_is_quote_status_id',
               'tweet_retweeted_status',
               'tweet_favorited',
               'tweet_retweeted',
               'tweet_possibly_sensitive',
               'search_tweets']

res_no_dupes = res.drop_duplicates(subset=['tweet_id'])
res_no_dupes.to_excel('data/tweets_complete.xlsx')

