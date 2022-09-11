import logging
import config
from analytics import Research


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)03d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='analytics.logs',
                        filemode='w',
                        encoding='UTF-8',
                        level=logging.DEBUG)
    logging.info('Started')
    research = Research(config.data_filename)
    try:
        anal = research.Analytics(research.file_reader())
    except Exception as ex:
        print(ex)
        logging.critical(ex)
        research.send_report_to_slack(config.webhook, config.failure_msg)
    else:
        counts = anal.counts()
        fractions = anal.fractions(counts)
        predict = anal.predict_random(config.num_of_steps)

        tails_pred = sum(map(lambda x: int(x[1]), predict))
        heads_pred = sum(map(lambda x: int(x[0]), predict))
        tails_pred = str(tails_pred) + (" tails" if tails_pred != 1 else " tail")
        heads_pred = str(heads_pred) + (" heads" if heads_pred != 1 else " head")

        report_text = config.report_template.format(observations_count=sum(counts),
                                                    tails_count=counts[1], heads_count=counts[0],
                                                    tails_chance=fractions[1], heads_chance=fractions[0],
                                                    num_of_steps=config.num_of_steps,
                                                    tails_pred=tails_pred, heads_pred=heads_pred)

        anal.save_file(report_text, 'report')
        research.send_report_to_slack(config.webhook, config.success_msg)

    logging.info('Finished')
