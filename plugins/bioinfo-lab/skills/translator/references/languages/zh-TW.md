# zh-TW: Taiwan Traditional Chinese (default language)

## Terms

* Technical terms stay in English in Chinese text: genome, assembly, long-read sequencing, heritability, GWAS, linkage disequilibrium, cross-validation. Never write 基因體, 組裝, 定序, 遺傳率, 變異, 表現型, 基因型, 全基因體關聯分析, and add no Chinese gloss or parentheses. This covers genetics, genomics, bioinformatics, statistics, breeding, machine learning, medicine, software, file formats, and metrics.
* A Chinese source that uses a Chinese technical term: translating to English, use the field's standard English term (verify it); translating to Chinese, keep the English term.
* Reference for Taiwan terminology: the National Academy for Educational Research (國家教育研究院) terminology database 樂詞網, https://terms.naer.edu.tw/. The page could not be fetched when this skill was written, so the vocabulary below is common usage and not verified against it; look terms up there when in doubt.

## Output rules

* Taiwan Traditional Chinese only, never Simplified characters or mainland vocabulary. Taiwan vocabulary: 預設, 品質, 網路, 影片, 軟體, 資料, 程式, 伺服器, 解析度.
* Full-width punctuation (，。、；：？！「」『』), consistent spacing between Chinese and Latin text, and English conventions for numbers with units (5 kb, 37 °C).
* Check with the `writing` lint script (OpenCC `s2twp`) before saving.

## Restructuring

* **Chinese to English**: Chinese often omits subjects, tense, number, and connectives; supply them from context, without changing meaning. Break long topic-comment sentences into short subject-verb-object sentences. Make agents explicit (*we*, *the model*). Choose singular or plural by the data. Replace noun-heavy Chinese chains with verbs. Use the field's standard sentence frames (e.g., "We sequenced…", "X was associated with Y (OR = 1.8, 95% CI 1.2–2.7)", "Here we show…" only when the source states a finding).
* **English to Chinese**: split long English sentences with stacked modifiers into short Chinese sentences in logical order; turn passive constructions into natural active or topic-first Chinese; avoid 被 chains and long pre-noun modifiers; avoid translationese (e.g., 「對於…而言」 and 「進行…的…」 patterns when a plain verb works: write 分析 not 進行分析). Keep one concept per sentence. Resolve English pronouns (*it, this, they*) into explicit nouns when Chinese would otherwise be unclear.

## Strength of claim

*顯示* ≈ *show*, *提示* / *暗示* ≈ *suggest*, *可能* ≈ *may*, *與…相關* ≈ *associated with*. Never upgrade association to causation or soften a finding.
