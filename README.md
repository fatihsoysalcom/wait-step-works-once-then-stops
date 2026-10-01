# Wait Step Works Once Then Stops

This example demonstrates why a 'wait step' in automation or code might work correctly once, but then fail on subsequent attempts. It illustrates a common flaw where the wait mechanism itself modifies or 'consumes' the condition it's waiting for, preventing future waits for the same condition from succeeding. A correct implementation is also shown, where the wait step only observes the condition, leaving its state management to external logic.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Bekleme Adımınız Bir Kez Çalışıyor, Sonra Neden Duruyor?](https://fatihsoysal.com/blog/bekleme-adiminiz-bir-kez-calisiyor-sonra-neden-duruyor/).

## License

MIT — see [LICENSE](LICENSE).
