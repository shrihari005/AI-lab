def evaluate_sentence(sentence, model):
    if isinstance(sentence, str):
        return model[sentence]
    
    op = sentence[0]
    
    if op == 'NOT':
        return not evaluate_sentence(sentence[1], model)
    elif op == 'AND':
        return evaluate_sentence(sentence[1], model) and evaluate_sentence(sentence[2], model)
    elif op == 'OR':
        return evaluate_sentence(sentence[1], model) or evaluate_sentence(sentence[2], model)
    elif op == 'IMPLIES':
        p = evaluate_sentence(sentence[1], model)
        q = evaluate_sentence(sentence[2], model)
        return (not p) or q

def evaluate_kb(kb, model):
    return all(evaluate_sentence(sentence, model) for sentence in kb)

def print_truth_table(kb, symbols):
    print(f"{'P':<6}{'Q':<6}{'R':<6}{'S1 (Q->P)':<12}{'S2 (P->~Q)':<13}{'S3 (Q|R)':<10}{'KB Status'}")
    print("-" * 65)
    
    kb_true_models = []
    
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                model = {'P': p, 'Q': q, 'R': r}
                s1 = evaluate_sentence(kb[0], model)
                s2 = evaluate_sentence(kb[1], model)
                s3 = evaluate_sentence(kb[2], model)
                kb_val = evaluate_kb(kb, model)
                
                status = "TRUE (Model)" if kb_val else "False"
                if kb_val:
                    kb_true_models.append(model)
                    
                print(f"{str(p):<6}{str(q):<6}{str(r):<6}{str(s1):<12}{str(s2):<13}{str(s3):<10}{status}")
                
    return kb_true_models

def check_entailment(kb_models, alpha, query_name):
    entailed = True
    for model in kb_models:
        if not evaluate_sentence(alpha, model):
            entailed = False
            break
    print(f"Does KB entail {query_name}? {entailed}")

if __name__ == "__main__":
    symbols = ['P', 'Q', 'R']
    
    kb = [
        ('IMPLIES', 'Q', 'P'),
        ('IMPLIES', 'P', ('NOT', 'Q')),
        ('OR', 'Q', 'R')
    ]
    
    print("--- TRUTH TABLE ---")
    valid_models = print_truth_table(kb, symbols)
    
    print("\n--- ENTAILMENT RESULTS ---")
    queries = {
        "R": 'R',
        "R -> P": ('IMPLIES', 'R', 'P'),
        "Q -> R": ('IMPLIES', 'Q', 'R')
    }
    
    for query_name, alpha in queries.items():
        check_entailment(valid_models, alpha, query_name)

    print()
    print("SHRIHARI SUDHAKAR BADIGER: 1BM25CS522")