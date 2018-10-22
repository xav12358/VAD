
import requests
import json
import os, sys
import youtube_dl
import multiprocessing


name_dataset = ['music',
'speech',
'vehicle',
'musical_instrument',
'plucked_string_instrument',
'singing',
'car',
'animal',
'outside_rural_or_natural',
'violin_fiddle',
'bird',
'drum',
'engine',
'narration_monologue',
'drum_kit',
'acoustic_guitar',
'dog',
'child_speech_kid_speaking',
'bass_drum',
'rail_transport',
'motor_vehicle_road',
'water',
'female_speech_woman_speaking',
'siren',
'railroad_car_train_wagon',
'tools',
'silence',
'snare_drum',
'wind',
'bird_vocalization_bird_call_bird_song',
'fowl',
'wind_instrument_woodwind_instrument',
'emergency_vehicle',
'laughter',
'chirp_tweet',
'rapping',
'cheering',
'gunshot_gunfire',
'radio',
'cat',
'hihat',
'helicopter',
'fireworks',
'stream',
'bark',
'baby_cry_infant_cry',
'snoring',
'train_horn',
'double_bass',
'explosion',
'crowing_cockadoodledoo',
'bleat',
'computer_keyboard',
'civil_defense_siren',
'bee_wasp_etc',
'bell',
'chainsaw',
'oink',
'tick',
'tabla',
'liquid',
'traffic_noise_roadway_noise',
'beep_bleep',
'frying_food',
'whack_thwack',
'sink_filling_or_washing',
'burping_eructation',
'fart',
'sneeze',
'aircraft_engine',
'arrow',
'giggle',
'hiccup',
'cough',
'cricket',
'sawing',
'tambourine',
'pump_liquid',
'squeak',
'male_speech_man_speaking',
'keyboard_musical',
'pigeon_dove',
'motorboat_speedboat',
'female_singing',
'brass_instrument',
'motorcycle',
'choir',
'race_car_auto_racing',
'chicken_rooster',
'idling',
'sampler',
'ukulele',
'synthesizer',
'cymbal',
'spray',
'accordion',
'scratching_performance_technique',
'child_singing',
'cluck',
'water_tap_faucet',
'applause',
'toilet_flush',
'whistling',
'vacuum_cleaner',
'meow',
'chatter',
'whoop',
'sewing_machine',
'bagpipes',
'subway_metro_underground',
'walk_footsteps',
'whispering',
'crying_sobbing',
'thunder',
'didgeridoo',
'church_bell',
'ringtone',
'buzzer',
'splash_splatter',
'fire_alarm',
'chime',
'babbling',
'glass',
'chewing_mastication',
'microwave_oven',
'air_horn_truck_horn',
'growling',
'telephone_bell_ringing',
'moo',
'change_ringing_campanology',
'hands',
'camera',
'pour',
'croak',
'pant',
'finger_snapping',
'gargling',
'inside_small_room',
'outside_urban_or_manmade',
'truck',
'bowed_string_instrument',
'medium_engine_mid_frequency',
'marimba_xylophone',
'aircraft',
'cello',
'flute',
'glockenspiel',
'power_tool',
'fixedwing_aircraft_airplane',
'waves_surf',
'duck',
'clarinet',
'goat',
'honk',
'skidding',
'hammond_organ',
'electronic_organ',
'thunderstorm',
'steelpan',
'slap_smack',
'battle_cry',
'percussion',
'trombone',
'banjo',
'mandolin',
'guitar',
'strum',
'boat_water_vehicle',
'accelerating_revving_vroom',
'electric_guitar',
'orchestra',
'wind_noise_microphone',
'effects_unit',
'livestock_farm_animals_working_animals',
'police_car_siren',
'rain',
'printer',
'drum_machine',
'fire_engine_fire_truck_siren',
'insect',
'skateboard',
'coo',
'conversation',
'typing',
'harp',
'thump_thud',
'mechanisms',
'canidae_dogs_wolves',
'chuckle_chortle',
'rub',
'boom',
'hubbub_speech_noise_speech_babble',
'telephone',
'blender',
'whimper',
'screaming',
'wild_animals',
'pig',
'artillery_fire',
'electric_shaver_electric_razor',
'baby_laughter',
'crow',
'howl',
'breathing',
'cattle_bovinae',
'roaring_cats_lions_tigers',
'clapping',
'alarm',
'chink_clink',
'ding',
'toot',
'clock',
'children_shouting',
'fill_with_liquid',
'purr',
'rumble',
'boing',
'breaking',
'light_engine_high_frequency',
'cash_register',
'bicycle_bell',
'inside_large_room_or_hall',
'domestic_animals_pets',
'bass_guitar',
'electric_piano',
'trumpet',
'horse',
'mallet_percussion',
'organ',
'bicycle',
'rain_on_surface',
'quack',
'drill',
'machine_gun',
'lawn_mower',
'smash_crash',
'trickle_dribble',
'frog',
'writing',
'steam_whistle',
'groan',
'hammer',
'doorbell',
'shofar',
'cowbell',
'wail_moan',
'bouncing',
'distortion',
'vibraphone',
'air_brake',
'field_recording',
'piano',
'male_singing',
'bus',
'wood',
'tap',
'ocean',
'door',
'vibration',
'television',
'harmonica',
'basketball_bounce',
'clicketyclack',
'dishes_pots_and_pans',
'crumpling_crinkling',
'sitar',
'tire_squeal',
'fly_housefly',
'sizzle',
'slosh',
'engine_starting',
'mechanical_fan',
'stir',
'children_playing',
'ping',
'owl',
'alarm_clock',
'car_alarm',
'telephone_dialing_dtmf',
'sine_wave',
'thunk',
'coin_dropping',
'crunch',
'zipper_clothing',
'mosquito',
'shuffling_cards',
'pulleys',
'toothbrush',
'crowd',
'saxophone',
'rowboat_canoe_kayak',
'steam',
'ambulance_siren',
'goose',
'crackle',
'fire',
'turkey',
'heart_sounds_heartbeat',
'singing_bowl',
'reverberation',
'clicking',
'jet_engine',
'rodents_rats_mice',
'typewriter',
'caw',
'knock',
'ice_cream_truck_ice_cream_van',
'stomach_rumble',
'french_horn',
'roar',
'theremin',
'pulse',
'train',
'run',
'vehicle_horn_car_horn_honking',
'clipclop',
'sheep',
'whoosh_swoosh_swish',
'timpani',
'throbbing',
'firecracker',
'belly_laugh',
'train_whistle',
'whistle',
'whip',
'gush',
'biting',
'scissors',
'clang',
'singlelens_reflex_camera',
'chorus_effect',
'inside_public_space',
'steel_guitar_slide_guitar',
'waterfall',
'hum',
'raindrop',
'propeller_airscrew',
'filing_rasp',
'reversing_beeps',
'shatter',
'sanding',
'wheeze',
'hoot',
'bowwow',
'car_passing_by',
'ticktock',
'hiss',
'snicker',
'whimper_dog',
'shout',
'echo',
'rattle',
'sliding_door',
'gobble',
'plop',
'yell',
'drip',
'neigh_whinny',
'bellow',
'keys_jangling',
'dingdong',
'buzz',
'scratch',
'rattle_instrument',
'hair_dryer',
'dial_tone',
'tearing',
'bang',
'noise',
'bird_flight_flapping_wings',
'grunt',
'jackhammer',
'drawer_open_or_close',
'whir',
'tuning_fork',
'squawk',
'jingle_bell',
'smoke_detector_smoke_alarm',
'train_wheels_squealing',
'caterwaul',
'mouse',
'crack',
'whale_vocalization',
'squeal',
'zither',
'rimshot',
'drum_roll',
'burst_pop',
'wood_block',
'harpsichord',
'white_noise',
'bathtub_filling_or_washing',
'snake',
'environmental_noise',
'string_section',
'cacophony',
'maraca',
'snort',
'yodeling',
'electric_toothbrush',
'cupboard_open_or_close',
'sound_effect',
'tapping_guitar_technique',
'ship',
'sniff',
'pink_noise',
'tubular_bells',
'gong',
'flap',
'throat_clearing',
'sigh',
'busy_signal',
'zing',
'sidetone',
'crushing',
'yip',
'gurgling',
'jingle_tinkle',
'boiling',
'mains_hum',
'humming',
'sonar',
'gasp',
'power_windows_electric_windows',
'splinter',
'heart_murmur',
'air_conditioning',
'pizzicato',
'ratchet_pawl',
'chirp_tone',
'heavy_engine_low_frequency',
'rustling_leaves',
'speech_synthesizer',
'rustle',
'clatter',
'slam',
'eruption',
'cap_gun',
'synthetic_singing',
'shuffle',
'wind_chime',
'chop',
'scrape',
'squish',
'foghorn',
'dental_drill_dentists_drill',
'harmonic',
'static',
'sailboat_sailing_ship',
'cutlery_silverware',
'gears',
'chopping_food',
'creak',
'fusillade',
'roll',
'electronic_tuner',
'patter',
'electronic_music',
'dubstep',
'techno',
'rock_and_roll',
'pop_music',
'rock_music',
'hip_hop_music',
'classical_music',
'soundtrack_music',
'house_music',
'heavy_metal',
'exciting_music',
'country',
'electronica',
'rhythm_and_blues',
'background_music',
'dance_music',
'jazz',
'mantra',
'blues',
'trance_music',
'electronic_dance_music',
'theme_music',
'gospel_music',
'music_of_latin_america',
'disco',
'tender_music',
'punk_rock',
'funk',
'music_of_asia',
'drum_and_bass',
'vocal_music',
'progressive_rock',
'music_for_children',
'video_game_music',
'lullaby',
'reggae',
'newage_music',
'christian_music',
'independent_music',
'soul_music',
'music_of_africa',
'ambient_music',
'bluegrass',
'afrobeat',
'salsa_music',
'music_of_bollywood',
'beatboxing',
'flamenco',
'psychedelic_rock',
'opera',
'folk_music',
'christmas_music',
'middle_eastern_music',
'grunge',
'song',
'a_capella',
'sad_music',
'traditional_music',
'scary_music',
'ska',
'chant',
'carnatic_music',
'swing_music',
'happy_music',
'jingle_music',
'funny_music',
'angry_music',
'wedding_music',
'engine_knocking'
]

base_url = 'https://storage.googleapis.com/audioset_website_data/youtube_corpus/v1/'
dataset_type = ['eval', 'balanced_train', 'unbalanced_train']
base_folder =  './data/'
youtube_base_url = 'https://www.youtube.com/watch?v='
base_file_name = './data/Youtube_'

def my_hook(d):

    id, _ = os.path.splitext(d['filename'])

    if d['status'] == 'finished':
        print('{}: saving info'.format(id))
        os.rename('{}.{}~'.format(id, INFO_EXT), '{}.{}'.format(id, INFO_EXT))
        print('{}: converting audio'.format(id))
    else:
        print('{}: {}\r'.format(id, d['_percent_str']), end="", flush=True)


def parse_list(url, folder):
    print('url {0}'.format(url) )
    r = requests.get(url, allow_redirects=True)
    content = r.content[2:-1].decode().replace('\\x27s','')
    print('content {0}'.format(content) )

    dictionnary = json.loads(content)
    # Generate list of video url
    video_list = []
    folder_list = []
    for video_name in dictionnary:
        video_list += [youtube_base_url + video_name[0]]
        folder_list += [folder]
    return video_list, folder_list


#################################################################################"
#################################################################################"
#################################################################################""
class MyLogger(object):

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


DOWNLOAD_DIR = './data/'
INFO_EXT = 'info'
default_opts = {
    'ignoreerrors' : True,
    'outtmpl': '{}%(extractor_key)s_%(id)s.%(ext)s'.format(DOWNLOAD_DIR),
    'format': 'bestaudio/best',
    'writesubtitles' : True,
    #'writeautomaticsub' : True,
    'download_archive' : 'archive',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def chunks(l, n):    
    for i in range(0, len(l), n):
        yield l[i:i + n]


def is_list(object):
    return type(object) is list or type(object) is set or type(object) is tuple



def download(urls, n_parallel=0, ydl_opts=default_opts, subtitles_only=False):

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    if not is_list(urls):
        urls = (urls,)

    if n_parallel <= 1 or len(urls) < n_parallel:
        _download(urls, ydl_opts=ydl_opts, subtitles_only=subtitles_only)
    else:
        pool = multiprocessing.Pool(n_parallel)
        tasks = []
        n_per_task = len(urls) // n_parallel
        for sub_urls in chunks(urls, n_per_task):
            tasks.append((sub_urls, ydl_opts, subtitles_only))
        results = [pool.apply_async(_download, t) for t in tasks]
        output = [p.get() for p in results]
    print('finished!')


def _download(urls, ydl_opts=default_opts, subtitles_only=False):

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        print('checking urls [{}]'.format(len(urls)))

        valid_urls = []
        for url in urls:
            print(url.encode('latin-1'), end="", flush=True)
            info_dict = ydl.extract_info(url, download=False)
            if not info_dict:
                print(' skip [not found]')
                continue
            if subtitles_only:
                if not 'subtitles' in info_dict or not info_dict['subtitles']:
                    print(' skip [no subtitles]')
                    continue
            print(' ok')
            with open(os.path.join(DOWNLOAD_DIR, '{}_{}.{}~'.format(info_dict['extractor_key'], info_dict['id'], INFO_EXT)), 'w') as fp:
                json.dump(info_dict, fp)
            valid_urls.append(url)

        print('start downloading [{}]'.format(len(valid_urls)))

        if valid_urls:
            ydl.download(valid_urls)

#################################################################################"
#################################################################################"
#################################################################################"



############## get all data

full_video_list  = []
full_folder_list = []
for name in name_dataset:
    for type_dat in dataset_type:
        # Create the local folder
        directory = os.path.join(base_folder, name, type_dat)
        if not os.path.exists(directory):
            os.makedirs(directory)

        url = base_url+ type_dat + '/'+ name + '/1.js'
        video_list, folder_list = parse_list(url, directory)

        index = 1

        while (index < len(video_list)):
            index_max = min(index +32, len(video_list) )
            len_block = index_max - index
            download(full_video_list[index:index_max], n_parallel=len_block, subtitles_only=False)
            index += 32
            break
        full_video_list += video_list
        full_folder_list += folder_list

print('full_video_list \n\n {0}'.format(full_video_list))


############ dispatch the data
for index in range(len(full_video_list)):
    video_name1 =  base_file_name +  (full_video_list[index])[32:] + '.webm'
    video_name2 =  base_file_name +  (full_video_list[index])[32:] + '.m4a'
    # print("video_name {0}  {1}".format(full_video_list[index], video_name))
    if os.path.isfile('./' + video_name1):
        os.rename(  video_name1, full_folder_list[index] + '/' + video_name1[7:])
        print( video_name1 +  ' exist and move to ' + full_folder_list[index] + '/' + video_name1[7:] )
    else:
         if os.path.isfile('./' + video_name2):
            os.rename(  video_name2, full_folder_list[index] + '/' + video_name2[7:])
            print( video_name2 +  ' exist and move to ' + full_folder_list[index] + '/' + video_name2[7:] )

    # else:
        # print( video_name +  'doesn t exist')
    index += 1
